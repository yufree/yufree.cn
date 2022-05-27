---
title: Using xcmsrocker on HPC via Singularity
author: Miao Yu
date: '2022-05-26'
slug: using-xcmsrocker-on-hpc-via-singularity
categories: []
tags: []
---

Docker should be the most popular container platform. Container distribution via dockerhub makes it easy to provide all-in-one development/data analysis environment for scientist. It's always a good idea to use container on the high performance computing (HPC) cluster to accelerate data processing. Since Docker provides root access to the system they are running on, it's always not allowed to be used on HPC. On the other hand, Singularity is more friendly to scientific research with MPI support, as well as security restriction.

I released [xcmsrocker](https://github.com/yufree/xcmsrocker) image for metabolomics data analysis for a long time and always said that it should be easy to deploy on HPC or cloud computing platform. It's always right for the latter options and you can use docker image on the most popular cloud. However, you will need some extra work for HPC.

The first issue is to build a Singularity image from a docker image hosted on Docker Hub. You need to load singularity module after login on HPC:

```
ml singularity
```

Then pull the xcmsrocker image

```
singularity pull docker://yufree/xcmsrocker:lastest
```

Now you will find a file with name 'xcmsrocker_latest.sif' in you home folder. If your HPC use slurm for job management, you can use the following job script and save as a file called "rstudio-server.job":

```
#!/bin/sh
#SBATCH --time=05:00:00
#SBATCH --signal=USR2
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8192
#SBATCH --output=/home/%u/rstudio-server.job.%j

# Create temporary directory to be populated with directories to bind-mount in the container
# where writable file systems are necessary. Adjust path as appropriate for your computing environment.
workdir=$(python -c 'import tempfile; print(tempfile.mkdtemp())')

mkdir -p -m 700 ${workdir}/run ${workdir}/tmp ${workdir}/var/lib/rstudio-server
cat > ${workdir}/database.conf <<END
provider=sqlite
directory=/var/lib/rstudio-server
END

# Set OMP_NUM_THREADS to prevent OpenBLAS (and any other OpenMP-enhanced
# libraries used by R) from spawning more threads than the number of processors
# allocated to the job.
#
# Set R_LIBS_USER to a path specific to rocker/rstudio to avoid conflicts with
# personal libraries from any R installation in the host environment

cat > ${workdir}/rsession.sh <<END
#!/bin/sh
export OMP_NUM_THREADS=${SLURM_JOB_CPUS_PER_NODE}
export R_LIBS_USER=${HOME}/R/xcmsrocker
exec rsession "\${@}"
END

chmod +x ${workdir}/rsession.sh

export SINGULARITY_BIND="${workdir}/run:/run,${workdir}/tmp:/tmp,${workdir}/database.conf:/etc/rstudio/database.conf,${workdir}/rsession.sh:/etc/rstudio/rsession.sh,${workdir}/var/lib/rstudio-server:/var/lib/rstudio-server"

# Do not suspend idle sessions.
# Alternative to setting session-timeout-minutes=0 in /etc/rstudio/rsession.conf
# https://github.com/rstudio/rstudio/blob/v1.4.1106/src/cpp/server/ServerSessionManager.cpp#L126
export SINGULARITYENV_RSTUDIO_SESSION_TIMEOUT=0

export SINGULARITYENV_USER=$(id -un)
export SINGULARITYENV_PASSWORD=$(openssl rand -base64 15)
# get unused socket per https://unix.stackexchange.com/a/132524
# tiny race condition between the python & singularity commands
readonly PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
cat 1>&2 <<END
1. SSH tunnel from your workstation using the following command:

   ssh -N -L 8787:${HOSTNAME}:${PORT} ${SINGULARITYENV_USER}@LOGIN-HOST

   and point your web browser to http://localhost:8787

2. log in to RStudio Server using the following credentials:

   user: ${SINGULARITYENV_USER}
   password: ${SINGULARITYENV_PASSWORD}

When done using RStudio Server, terminate the job by:

1. Exit the RStudio Session ("power" button in the top right corner of the RStudio window)
2. Issue the following command on the login node:

      scancel -f ${SLURM_JOB_ID}
END

singularity exec --cleanenv xcmsrocker_latest.sif \
    rserver --www-port ${PORT} \
            --auth-none=0 \
            --auth-pam-helper-path=pam-helper \
            --auth-stay-signed-in-days=30 \
            --auth-timeout-minutes=0 \
            --server-user XXX \
            --rsession-path=/etc/rstudio/rsession.sh
printf 'rserver exited' 1>&2
```

This file is modified from [Rocker's singularity tutorial](https://www.rocker-project.org/use/singularity/).

Here, you need to change `--server-user XXX` to the user name for your HPC. For example, my user name to login HPC is 'yufree' and I will set `--server-user yufree`. This option will make sure you can login in your RStudio server and the default user don't have access.

Then submit this job to HPC:

```
$ sbatch rstudio-server.job
```

Then you should see a file with job ID as extension such as 'rstudio-server.job.xxxxxxx' in your HPC home folder. 'xxxxxxx' is your job ID. Then you can check the content in this file:

```
cat rstudio-server.job.xxxxxxx
```

You will find the user name, password and port information on HPC. The user name should be the same as you HPC user name and password will change anytime you submit this job. 

To access RStudio on your local computer, you need to bind your local port to the running HPC port. You need to open a new terminal to establish the SSH tunnel:

```
ssh -N -L 8787:[YOUR_PORT_INFORMATION] [HPC_USERNAME]@[HPC domain]
```

Here the port information is from `rstudio-server.job.xxxxxxx`. `[HPC_USERNAME]@[HPC domain]` is the same with the regular ssh information to login in HPC. This command will forward HPC's port to port 8787 on your local computer. After you open the SSH tunnel, you can access the RStudio from xcmsrocker via your own browser: http://localhost:8787

Now you can enjoy your xcmsrocker image on HPC. Keep in mind that only the packages supporting parallel computing would get benefits from HPC resources. If the software doesn't support parallel computing, you will need to modify their source code or it will be a waste of time to run them on HPC.

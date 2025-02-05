---
title: AI论文评分
author: Miao Yu
date: '2025-02-04'
slug: ai-score-paper
categories: []
tags:
  - idea
  - tech
---
作为成年男性，每个月我都会有那么一两天坐立不安，没错，就是更新研究速递。本项目初衷就是每个月推送些我读到感兴趣的环境科学领域的论文，是在GitHub上收集投稿，不过显然我高估了投稿热情，所以一到月底我就不得不拿出半天一天的时间把过去一个月发表的相关论文过一遍。本来这倒也不算是负担，毕竟吃这碗饭就得保持对前沿的敏感，但项目持续七年了，怎么说也要有个七年之痒了。

我大体计算了一下，现在每个月我收到的更新条目大概有五百条左右，九成看完题目我就过了，剩下几十条会读摘要，推荐出来的基本都会读原文。然而，就算这样，月底也得搞几个小时，我应该雇个助手来帮我筛掉那九成文章。当然，我雇不起人，但大语言模型我还是雇得起的，我平时很多文章只看了题目，但要是大语言模型就可以至少读完摘要，那么我需要做的就是让他给我出一个推荐，为了量化方便，就让他直接打分。

因为研究速递面向的读者比较宽泛，所以我设计了两个分数，一个直接考察其学术价值，另一个考察其社会影响力。前者是要保证质量过硬，后者则是要排除掉那些小圈子互捧臭脚的无用研究。最开始的评分是这两个分的加权综合分，后来我还是改成了分项得分，毕竟我也想看看那些影响力大但学术价值低或学术价值高但不说人话的研究。

设计好提示词后，剩下的就是自动化部署，我首选是GitHub Action配合cron任务，设计周期是一周运行一次，这样我也就把月底的几个小时均摊到了每周一两个小时。然后输出就是GitHub的issue，直接推送到环境黑板报的仓库那边。本来我是想输出包括摘要与评分的，但测试了下发现issue有字数限制，所以就把输出改成了标题与评分。这样每周第一天，我就会收到过去一周新发表文章的AI评分，然后会参考评分去读文献。

之所以要AI评分，主要是我自己水平无法覆盖环境科学全领域，有些东西看不懂。另外AI评分可以规避掉大多数水文，要知道即便是顶级期刊，上面的文章被引用分布也是严重左偏的，影响因子其实是被少数高质量文章撑起来的。这就是所谓新手谈期刊而老手谈引用的现象，肯定是哪个高谈哪个。AI评分就会规避掉一些编辑的人情文章，另外就是一些公众不关心的研究。我并不是说不被关心的研究领域就不重要，但研究速递毕竟不是学术期刊，自然要考虑社会影响力这个维度。

设计好思路就要谈成本了。API的调用无论如何都是要花钱的，但并不贵，这里我用的是Open AI的GPT-4o-mini。不是我不想用deepseek，只是那个网站API的页面我一直都没打开，不知道是不是对海外IP做了限制。我大体计算了一下，每月大概两三块人民币，一年不超过三十块，这笔钱我就走指北奖学金了，这个破奖学金虽然还没达到启动标准，但每年的利息似乎已经够这个项目开支了。

当然，这一定也是个开源项目，最简单的复现方式就是新建一个仓库，然后新建 `.github/workflows` 文件夹，里面写个这样的`yaml`文件：

```yaml
name: Weekly Article
on:
  schedule:
    - cron: '0 0 * * 0'
  workflow_dispatch:

jobs:
  run_script:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: pip install feedparser requests openai

      - name: Run Python Script
        run: python update.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          
```

这里要注意，你要在你仓库的环境里设置 `OPENAI_API_KEY`这个环境变量，上面那个 `workflow_dispatch:` 是用来让你可以手动启动这个流程，不然就是每周自动运行一次。

在仓库里，你要放一个 `update.py` 的文件，里面代码如下：

```
import feedparser
from datetime import datetime, timedelta, timezone
import json
import requests
import os
import openai

# Example PubMed RSS feed URL
rss_url = 'https://pubmed.ncbi.nlm.nih.gov/rss/search/12cYCaYYmd3PKH1TcODuh5Cr7776fWscbUhYnAwoSRATXNoE-E/?limit=100&utm_campaign=pubmed-2&fc=20250204112327'

access_token = os.getenv('GITHUB_TOKEN')
openaiapikey = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key=openaiapikey)

def extract_scores(text):
    # Use OpenAI API to get Research Score and Social Impact Score separately
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an environmental science expert and researcher. You are skilled at selecting interesting/novelty research."},
            {"role": "user", "content": f"Given the text '{text}', evaluate this article with two scores:\n"
                                        "1. Research Score (0-100): Based on research innovation, methodological rigor, and data reliability.\n"
                                        "2. Social Impact Score (0-100): Based on public attention, policy relevance, and societal impact.\n"
                                        "Provide the scores in the following format:\n"
                                        "Research Score: <score>\n"
                                        "Social Impact Score: <score>"}
        ],
        max_tokens=100,
        temperature=0.5
    )

    generated_text = response.choices[0].message.content.strip()  

    # Extract research score
    research_score_start = generated_text.find("Research Score:")
    research_score = generated_text[research_score_start+len("Research Score:"):].split("\n")[0].strip()

    # Extract social impact score
    social_impact_score_start = generated_text.find("Social Impact Score:")
    social_impact_score = generated_text[social_impact_score_start+len("Social Impact Score:"):].strip()

    return research_score, social_impact_score

def get_pubmed_abstracts(rss_url):
    abstracts_with_urls = []

    # Parse the PubMed RSS feed
    feed = feedparser.parse(rss_url)

    # Calculate the date one week ago
    one_week_ago = datetime.now(timezone.utc) - timedelta(weeks=1)

    # Iterate over entries in the PubMed RSS feed and extract abstracts and URLs
    for entry in feed.entries:
        # Get the publication date of the entry
        published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z')

        # If the publication date is within one week, extract the abstract and URL
        if published_date >= one_week_ago:
            # Get the abstract and DOI of the entry
            title = entry.title
            abstract = entry.content[0].value
            doi = entry.dc_identifier
            abstracts_with_urls.append({"title": title, "abstract": abstract, "doi": doi})

    return abstracts_with_urls

# Get the abstracts from the PubMed RSS feed
pubmed_abstracts = get_pubmed_abstracts(rss_url)

# Create an empty list to store each abstract with its scores
new_articles_data = []

for abstract_data in pubmed_abstracts:
    title = abstract_data["title"]
    research_score, social_impact_score = extract_scores(abstract_data["abstract"])
    doi = abstract_data["doi"]

    new_articles_data.append({
        "title": title,
        "research_score": research_score,
        "social_impact_score": social_impact_score,
        "doi": doi
    })
    
# Create issue title and content
issue_title = f"Weekly Article Matching - {datetime.now().strftime('%Y-%m-%d')}"
issue_body = "Below are the article matching results from the past week:\n\n"

for article_data in new_articles_data:
    abstract = article_data["title"]
    research_score = article_data["research_score"]
    social_impact_score = article_data["social_impact_score"]
    doi = article_data.get("doi", "No DOI available")  # Default to "No DOI available" if DOI field is missing

    issue_body += f"- **Title**: {abstract}\n"
    issue_body += f"  **Research Score**: {research_score}\n"
    issue_body += f"  **Social Impact Score**: {social_impact_score}\n"
    issue_body += f"  **DOI**: {doi}\n\n"

def create_github_issue(title, body, access_token):
    url = f"https://api.github.com/repos/yufree/hjhbb/issues"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        print("Issue created successfully!")
    else:
        print("Failed to create issue. Status code:", response.status_code)
        print("Response:", response.text)

# Create the issue
create_github_issue(issue_title, issue_body, access_token)
```

这段代码里的`rss_url` 请改成你关心的期刊，最好用pubmed上rss生成的功能，有些出版社的rss不带摘要。另外就是也要改掉提示词里相关学科，不然它还是一个只关心环境科学的AI。设置好了后就可以洗洗睡了，以后每周一就会在这个仓库的issue里看到最新文章的评分。

~~另外如果你足够懒，可以直接fork环境黑板报的仓库<https://github.com/yufree/hjhbb> ，只保留上面提到的两个文件，加上自己API，修改提示词后就可以用了。~~

如果你跟我一样懒，直接用这个模版即可，记得按用法修改：<https://github.com/yufree/autoaiscore>

这当然可以魔改成其他形式，例如对开放获取文章进行总结、对感兴趣领域新闻进行个性化评分、对一组新文章进行关键词相关知识的提取等。这其实就是所谓智能代理的一个乞丐版，本质就是大语言模型对接定时任务与RSS更新来提供简报。先用在这个领域主要是论文的格式比较统一，处理rss上比较简单。未来如果你想用好大语言模型，可能最先需要的就是了解如何给语言模型对接上其他工具，整合到自己的目标项目里。

我是ifttt的第一批用户，那时的口号就是让互联网为你打工。就目前模型的价格而言，这种尝试近乎免费，请放飞想象力。

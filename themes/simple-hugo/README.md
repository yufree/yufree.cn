# Alert
Work in progress.

# Simple Hugo
A simple [hugo](http://gohugo.io/) theme.

#### Params
- For add new links on navbar see ```[params.links]```.
```toml
[params]
  github = "username"
  twitter = "username"
  email = "email"
  shortDescription = "yada yada yada"
  [params.links]
    [params.links.About]
      "url" = "/about/"
      "title" = "About"
    [params.links.ContactMe]
      "url" = "/contact/"
      "title" = "Contact Me"
```

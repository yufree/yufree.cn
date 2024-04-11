---
title: 半自动综述
author: Miao Yu
date: '2024-04-10'
slug: semi-auto-review
categories: []
tags:
  - metabolomics
  - tech
---
作为一个审过写过综述的科研人员，我一直希望不要有那么多综述。原因有二，一是大多数综述只综不述，好一点还知道来个荟萃分析，懒得连图都没有，单纯就是把过去一段时间发表论文转述一遍；另一个问题是很多新兴领域文章很少，此时发表的不算综述而应该是前瞻，这类文章论据相对比较少，价值也有限。我读博士的时候曾经用过一个很长的word文档与在线幻灯片来记录我读文献的摘要，这些东西在我写博士论文第一章时非常有用。16年我博士毕业出国做博后，此时我就不太喜欢长文档这种形式了，然后我启动了一个草台班子项目，就是在线研究笔记本[metaworkflow](https://bookdown.org/yufree/Metabolomics/)这个Github项目，不用藏着掖着，咱就喜欢打明牌。

简单说，这个项目就是以我理想中的综述作为框架搭起来，形式上就是一本在线电子书，主要是代谢组学数据处理相关的内容。主要是平时读文献看到有意思的加到里面了，有些则是我投稿被反复折腾后我懒得改的内容。因为这是全公开的电子书，我加入了参考文献链接，方便读者溯源。不过我很也反感网页去按学术期刊列参考文献的装腔行为，互联网时代请直接给原文链接，反正真正关心的也会复制文末那一坨直接搜，不如大家都轻松些，别绕弯子。

这个草台项目纯属个人兴趣，也收到过邮件问要不要直接出版，我直接否定，因为这本书内容更新会非常频繁。事实上，每年我会加入约40篇左右我读过认为有价值或以后可能会引用的新工作，这件事一直持续到现在。去年我更新的时候，推特上有朋友说不错，我当时沉迷ChatGPT，就回复说明年我可能要让ChatGPT来给我更新。结果今年我还是手动更新了这份笔记，但更新完后我痛定思痛，觉得是时候让人工智能来给我干活了。

首先，目前这份在线文档内容已经相对丰富了，不同章节间关注的点不一样。其次，我所谓的更新，实质上就是通过学术搜索引擎提供的RSS订阅拿到最新文章，一大半文章我看个题目就过了，剩下的看摘要，看全文的也就十分之一，之后觉得有价值的大概又是三分之一，到最后也就平均一周能看到一篇我真正觉得值得更新的新东西，这个过程其实可以自动化。最后，我之所以不打算搞全自动的在线综述是因为我还是需要决定最后是否将某篇文章加进来。

有了上述三点想法，实现起来就很轻松了。首先，我接入ChatGPT的API，让他对我已有电子书的二级三级标题下的文本内容提取十个关键词，这样可以保证章节间有足够差异。然后，我写了个脚本，自动读取最近更新的RSS链接，解析出摘要、网址并再次接入ChatGPT接口总结十个这篇文章的关键词并用一句话总结出摘要，这其实就是我之前做的事。之后，写一个简单的匹配函数来匹配新论文关键词与已有的章节关键词，保留相似度最高的章节。最后，将匹配成功的文章连同摘要、一句话总结与匹配章节组合成一个issue，通过GitHub actions里的定时任务自动推送到我这个仓库，由我来决定是否要把文章加入笔记，而需要加入的内容，大概率就是那个一句话总结。

考虑到章节的关键词更新比较少，我就直接离线跑了个脚本，生成了json文件扔到仓库根目录下，下面是相关脚本。这里我是分章节提取后重组为一个文件，主要是懒得写循环。当然，这是蟒蛇代码。

```python
from openai import OpenAI
import requests
import json
import re
def clean_text(text):
    cleaned_text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    cleaned_text = re.sub(r'\[\@[\w-]+\]', '', cleaned_text)
    return cleaned_text

client = OpenAI(
    # This is the default and can be omitted
    api_key='替换成你的API',
)

def extract_keywords(text):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"You are an expert in metabolomics, mass spectrometry and analytical chemistry, extract 10 keywords from the text without numbering and separate them by comma and keywords should not include Mass spectrometry, analytical chemistry, metabolomics: '{text[:4000]}'",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5
    )
    keywords = [choice.text.strip() for choice in response.choices]
    return keywords

def extract_markdown_chapters(ebook_url):
    response = requests.get(ebook_url)
    markdown_text = response.text

    chapter_pattern = re.compile(r'(#{2}\s+.+)\n((?:[^#]+|\n)*(?:(?:^#{3}\s+.+)(?:[^#]+|\n)*)*)')
    chapters = chapter_pattern.findall(markdown_text)

    extracted_chapters = {}
    for second_level_title, third_level_content in chapters:
        second_level_title = second_level_title.strip()
        third_level_content = third_level_content.strip()

        cleaned_third_level_content = clean_text(third_level_content)
        chapter_keywords = extract_keywords(cleaned_third_level_content)

        if chapter_keywords:
            extracted_chapters[second_level_title] = {
                'content': cleaned_third_level_content,
                'keywords': chapter_keywords
            }

    return extracted_chapters

def save_chapter_keywords(chapters, filename):
    with open(filename, 'w') as f:
        json.dump(chapters, f, indent=4)

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/01-introduction.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'introduction_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/02-doe.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'doe_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/03-pretreatment.Rmd"

save_chapter_keywords(book_chapters, 'pretreatment_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/04-instrumental.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'instrumental_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/05-workflow.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'workflow_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/06-rawdata.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'rawdata_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/07-annotation.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'annotation_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/08-omics.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'omics_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/09-normalization.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'normalization_keywords.json')

ebook_url = "https://raw.githubusercontent.com/yufree/metaworkflow/master/10-statistics.Rmd"
book_chapters = extract_markdown_chapters(ebook_url)

save_chapter_keywords(book_chapters, 'statistics_keywords.json')

import json
import os

def merge_json_files(folder_path):
    merged_data = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                merged_data.update(data)

    return merged_data

folder_path = '.'
merged_json = merge_json_files(folder_path)
output_file_path = 'merged_file.json'
with open(output_file_path, 'w') as output_file:
    json.dump(merged_json, output_file, indent=4)

print("JSON files merged and saved to:", output_file_path)
```

这样通过我设定的每周日更新计划，过去一周RSS链接新出现的文章就可以自动被提取关键词并进行章节匹配，其实说白了就是为了节省点每次提取关键词的token，到这里这个半自动项目就跑通了。这个项目可以用来轻量级半自动维护一篇每周更新的综述，通过更换RSS地址也可以用来追踪其他内容。开发过程大概三天，耗资高达不到1美元。

如果你想复现这个项目，只需要关注这个仓库下那个update.py的脚本跟.github文件夹里update.yml这个文件，py文件里RSS地址可以改成你的，我这里用的pubmed的。当然，最大的困难可能是你得有个能产生章节差异的在线电子文档。不过这也不难，找一篇你读着最舒服的综述，然后分章节提取关键词生成一个json文件就可以了。上面或里面代码如果看不懂就问人工智能就行，反正很多函数也是他生成的。想启动一个长期项目最好的时间点是十年前，其次是现在。

其实我最开始设想的是让ChatGPT读完书全文与新文章全文后自己决定加入到哪里的，然后直接做一个定位推送，直接精准更新到相关章节的段落里。但一来很多文章没全文，二来这个玩法有点小贵，毕竟每次都要读全文。我当然可以预训练一个模型出来，但窃以为关键词能匹配上就可以转人工了，不然我担心ChatGPT会漏掉一些只有人能识别的东西。其实做成这样就已经排除掉大多数无关研究了，关键词越多效果越好，但个人项目就不那么折腾了。你要不在乎钱，模型换成GPT-4并用全文匹配效果可能更好，我没测试过，你得自己去化缘折腾。

我做半自动综述的最初动机就是希望这个项目哪怕我后面换了研究方向也能持续下去，这就好像我种下一株树苗，最后长成啥样其实我也不知道。欢迎各位看官围观改进，里面代码写的稀烂，但至少已经成功推送了一次[更新](https://github.com/yufree/metaworkflow/issues/20)，标志着我对ChatGPT进行了第一次周期性奴役。

项目地址：https://github.com/yufree/metaworkflow

本项目由大概率无法启动的指北奖学金沉淀资金的利息资助。

---
title: YuGPT上线
author: Miao Yu
date: '2024-04-01'
slug: yugpt
categories: []
tags:
  - life
---
经过快一年的研发，我宣布拟我型人工智能YuGPT今天正式上线。

该模型整合了当前所有开源最新大语言模型，用我的博客及不公开笔记作为语料训练，理论上可以回答世界上一切我了解的问题，回答口气也最大程度模拟了我个人风格。训练在万张显卡集群阵列下完成，耗时1008小时，经个人测试效果拔群，不限制输入文本数量，没有任何伦理审核，纯原生无污染，适合研究人员使用，欢迎试用：

<div id="container">
    <h3>YuGPT：问我啥都行</h1>
    <div id="response"></div>
    <input type="text" id="question" placeholder="请输入你的问题">
    <button onclick="getResponse()">提问</button>
</div>

<script>
    function getResponse() {
        var question = document.getElementById("question").value;
        var responseDiv = document.getElementById("response");
        responseDiv.innerHTML = "我仅代表于有理无理虚数欧氏非欧几何数群论热力磁光声量子原子氢氦锂铍硼碳氮氧氟氖钠镁铝硅磷硫氯氩钾钙分子细胞组织器官种属科界纲门植物动物家庭社区城市国家生态圈地球太阳系银河系宇宙水气声渣微生物循环经济气候变化环境法金木水火土临兵斗者皆阵列前行大慈大悲观世纪福音天主东正伊斯兰飞天拉面经史子集都没搞懂所以很水向您通知：节日快乐！";
    }
</script>

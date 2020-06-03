#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/5/19 22:27
# @Author: max liu
# @File  : demo_001.py

'''
https://amueller.github.io/word_cloud/auto_examples/masked.html#sphx-glr-auto-examples-masked-py
https://www.jianshu.com/p/e4b24a734ccc
https://zhuanlan.zhihu.com/p/28954970
https://yq.aliyun.com/articles/395614
'''

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np

#  输入数据源
# filename = "COVER-1.TXT"
filename = "demo_001.txt"

with open(filename) as f:
    mytext = f.read()

#  分词
mytext = " ".join(jieba.cut(mytext))
# 字体路径
font_path = "simsun.ttf"
# 背景图片
alice_mask = np.array(Image.open("alice_mask.png"))
# 自定义文字
stopwords = set(STOPWORDS)
# stopwords.add("said")
wordcloud = WordCloud(background_color="white", font_path=font_path, max_words=2000, stopwords=None, mask=alice_mask, contour_width=3, contour_color='steelblue').generate(mytext)

# store to file
wordcloud.to_file("alice.png")

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.show()
#  测试 test

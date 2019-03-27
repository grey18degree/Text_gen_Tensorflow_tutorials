import tensorflow as tf
import numpy as np
import os
import time
import jieba
import pandas as pd

'''
path_to_file = tf.keras.utils.get_file('/home/jing/data_set/finance_news.csv')

# 读取数据
text = open(path_to_file).read()
'''
# pandas 读取数据
finance_text = pd.read_csv('/home/jing/data_set/finance_news.csv', encoding='utf-8')
finance_text = finance_text.dropna()
print('Length of text:{} characters'.format(len(finance_text)))

#
finance = finance_text.content.values[:]
'''
print([i for i in jieba.cut(finance[1])])
'''
# 停用词
stopwords = pd.read_csv('/home/jing/data_set/stopwords.txt', encoding='utf-8', index_col=False, quoting=3, sep='\t', names=['stopword'])
stopwords = stopwords['stopword'].values

# 构建数据集
def preprocess(content, sentences):
    for line in content:
        try:
            segs = jieba.cut(line)
            segs = filter(lambda x: len(x)>1, segs)
            segs = filter(lambda x: x not in stopwords, segs)
            sentences.append(' '.join(segs))
        except Exception as e:
            print("Error:" + str(e))
            continue

sentences=[]
preprocess(finance, sentences)

# print(sentences[:2])

out = open('/home/jing/data_set/jieba_finance.txt', 'w')
for sentence in sentences:
    out.writelines(sentence)
print('done!')

jieba_read_text_finance = pd.read_csv('/home/jing/data_set/jieba_finance.txt', encoding='utf-8')
print(jieba_read_text_finance[:20])


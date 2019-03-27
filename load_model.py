from gensim.models import word2vec
model = word2vec.Word2Vec.load('/home/jing/data_set/finance.model')

y1 = model.similarity('中国', '国际')
y2 = model.most_similar('股票', topn=20)
print(y2)
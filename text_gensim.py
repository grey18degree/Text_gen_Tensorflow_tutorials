from gensim.models import word2vec

sentences = word2vec.Text8Corpus('/home/jing/data_set/jieba_finance.txt')
model = word2vec.Word2Vec(sentences, size=200)
model.save('/home/jing/data_set/finance.model')
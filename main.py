import pandas as pd
import os
import jieba.posseg as jb

from gensim import corpora, models
from pathlib import Path as path

from corpus import Corpus


# TODO: set data_fold and stopwords
cur_corpus = Corpus(path('./sample_txt/'), stopwords=['你', '我', '他'])

print('start generating dictionary')
dictionary = corpora.Dictionary(cur_corpus)
print('finish generating dictionary')
cur_corpus.dic = dictionary

print('start training model')
# TODO: set num_topics
lda_model = models.LdaModel(corpus=cur_corpus, id2word=dictionary, num_topics=10)
print('finish training model')

for topic in lda_model.print_topics(num_words=100):
    print(topic)
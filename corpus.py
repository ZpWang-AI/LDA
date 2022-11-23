import re
import os
import jieba as jb
import jieba.posseg as jbp

from tqdm import tqdm 
from pathlib import Path as path


class Corpus:
    def __init__(self, root_fold, 
                 stopwords=('没', '就', '知道', '是', '才', '听听', '坦言', '全面', '越来越', '评价', '放弃', '人'),
                 tags=('n', 'nr', 'ns', 'nt', 'eng', 'v', 'd'),
                 ) -> None:
        self.root_fold = path(root_fold)
        self.stopwords = stopwords
        self.tags = tags
        self.dic = None
        
    def __iter__(self):
        return self.get_iter()
    
    def split_line(self, line):
        return re.split(r'[.!?。！？…]', line)
    
    def cut_sentence(self, sentence):
        return [w for w in jb.cut(sentence) if w not in self.stopwords]
        # return [w.word for w in jbp.cut(sentence) if w.flag in self.tags and w.word not in self.stopwords]
    
    def read_txt(self, file_path):
        with open(file_path, 'r', encoding='utf-8')as f:
            total_line = ''.join([line.strip() for line in f.readlines()])
            for sentence in self.split_line(total_line):
                yield sentence
    
    def get_iter(self):
        for son_file in tqdm(os.listdir(self.root_fold)):
            cur_file = self.root_fold/son_file
            for sentence in self.read_txt(cur_file):
                sentence = sentence.strip()
                if sentence:
                    sentence = self.cut_sentence(sentence)
                    if self.dic is None:
                        yield sentence
                    else:
                        yield self.dic.doc2bow(sentence)
                

if __name__ == '__main__':
    for a in Corpus('./data_txt/'):
        print(a)
    
from collections import defaultdict


def cal_co_occurrence(corpus, dic):
    res = defaultdict(int)
    for sentence in corpus:
        for p in range(len(sentence)-1):
            word1 = 
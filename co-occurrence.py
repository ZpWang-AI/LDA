from collections import defaultdict

from corpus import Corpus


def cal_co_occurrence(corpus: Corpus, dic: set):
    """calculate Co-Occurrence 

    Args:
        corpus (Corpus): iterator of list of words
        dic (set): a set that contains key words

    Returns:
        list: list of [word1, word2, weight]
    """
    res = defaultdict(int)
    for sentence in corpus:
        for p in range(len(sentence)-1):
            word1 = sentence[p]
            word2 = sentence[p+1]
            # TODO: filter pairs of word that would be considered
            if word1 in dic or word2 in dic:
                res['#'.join(sorted([word1, word2]))] += 1
    return [[*k.split('#'), v] for k, v in res.items()]
                
                
if __name__ == '__main__':
    sample_corpus = Corpus('./data_txt/', stopwords=('你', '我'))
    sample_dic = {'祖国', '党'}
    print(cal_co_occurrence(sample_corpus, sample_dic))
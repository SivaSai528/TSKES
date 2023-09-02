import nltk
import pprint
import itertools
import re
import pke
import string

def keywords_from_input(g_input):
    store=[]
    reciver = pke.unsupervised.MultipartiteRank()
    reciver.load_document(input=g_input)
    pos = {'PROPN'}
    reciver.candidate_selection(pos=pos)
    reciver.candidate_weighting()
    store_key = reciver.get_n_best(n=20)

    for item in store_key:
        store.append(item[0])

    return store

def final_keyword(text,summary):
    kw = keywords_from_input(text) 
    final_keywords=[]
    for k in kw:
        if k.lower() in summary.lower():
            final_keywords.append(k)
    return final_keywords
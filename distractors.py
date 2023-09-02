import requests
import json
import re
import random
from pywsd.similarity import max_similarity as mxs
from pywsd.lesk import adapted_lesk as adl
from pywsd.lesk import simple_lesk
from pywsd.lesk import cosine_lesk
from nltk.corpus import wordnet as wn


def gdw(x,text):

    options_=[]

    text= text.lower()

    given_text = text

    if len(text.split())>0:

        text = text.replace(" ","_")
    hy = getattr(x, "hypernyms")()
    if not hy: 

        return options_
    
    xy=getattr(hy[0], "hyponyms")()

    for x in xy:
        name = x.lemmas()[0].name()
        if name == given_text:
            continue
        name = ' '.join(word.capitalize() for word in name.replace("_", " ").split())

        if name is not None:
            if name not in options_:
                options_.append(name)
    return options_



def gws(s,text):
    text= text.lower()
    x=  len(text.split())
    if x>0:

        text = text.replace(" ","_")
    
    
    sy = wn.synsets(text,'n')
    if sy:
        wup = mxs(s, text, 'wup', pos='n')
        adlo =  adl(s, text, pos='n')
        lowest_index = min (sy.index(wup),sy.index(adlo))
        return sy[lowest_index]
    else:
        return None

def gdc(text):
    text = text.lower()
    ow= text
    if (len(text.split())>0):
        text = text.replace(" ","_")
    dl = [] 
    url = "http://api.conceptnet.io/query?node=/c/en/%s/n&rel=/r/PartOf&start=/c/en/%s&limit=5"%(text,text)
    obj = requests.get(url).json()

    for edge in obj['edges']:
        l = edge['end']['term'] 

        url2 = "http://api.conceptnet.io/query?node=%s&rel=/r/PartOf&end=%s&limit=10"%(l,l)
        obj2 = requests.get(url2).json()
        for edge in obj2['edges']:
            text2 = edge['start']['label']
            if text2 not in dl and ow.lower() not in text2.lower():
                dl.append(text2)
                   
    return dl

def gdo(ksm):
    kdl = {}

    for k in ksm:
        s = ksm[k]
        d = []
        for sent in s:
            wds = gws(sent, k)
            if wds:
                dt = gdw(wds, k)
                if len(dt) == 0:
                    dt = gdc(k)
                d.extend(dt)
            else:
                dt = gdc(k)
                d.extend(dt)
        if len(d) != 0:
            kdl[k] = d

    return kdl
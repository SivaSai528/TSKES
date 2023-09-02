from keywords_extraction import final_keyword,keywords_from_input
from sentence_mapping import context_input,context_kw
from distractors import gdc,gdo,gdw,gws
from Esummary import load_model, summarize_text
import nltk
import pprint
import itertools
import re
import pke
import string
from nltk.corpus import stopwords
from summarizer import Summarizer
from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor
import requests
import json
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from pywsd.lesk import simple_lesk
from pywsd.lesk import cosine_lesk
from nltk.corpus import wordnet as wn


summarizer_model = load_model('summarizer_model.pkl')
def MCQs(text):
    summarizer_model = load_model('summarizer_model2.pkl')
    summary = summarize_text(text, summarizer_model)

    filtered_keys=final_keyword(text,summary)
    sentences = context_input(summary)
    keyword_sentence_mapping = context_kw(filtered_keys, sentences)

    key_distractor_list = gdo(keyword_sentence_mapping)

    mcq_list = []
    index = 1
    for each in key_distractor_list:
        sentences = keyword_sentence_mapping[each]
        pattern = re.compile(each, re.IGNORECASE)
        for sentence in sentences:
            output = pattern.sub(" _______ ", sentence)
            mcq_list.append("%s) %s" % (index, output))
            choices = [each.capitalize()] + key_distractor_list[each]
            top4choices = choices[:4]
            random.shuffle(top4choices)
            optionchoices = ['a', 'b', 'c', 'd']
            correct_answer = optionchoices[top4choices.index(each.capitalize())]
            for idx, choice in enumerate(top4choices):
                mcq_list.append("\t%s) %s" % (optionchoices[idx], choice))
            mcq_list.append("\tCorrect Answer: %s) %s" % (correct_answer, each.capitalize()))
            index += 1

    return mcq_list
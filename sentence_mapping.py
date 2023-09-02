from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor

def context_input(g_input):
    context = [sent_tokenize(g_input)]
    context = [y for x in context for y in x]
    context = [f.strip() for f in context if len(f) > 15]
    return context

def context_kw(kw, contexts):
    kwp = KeywordProcessor()
    kws = {}
    for x in kw:
        kws[x] = []
        kwp.add_keyword(x)
    for context in contexts:
        kwf = kwp.extract_keywords(context)
        for x in kwf:
            kws[x].append(context)

    for y in kws.keys():
        v = kws[y]
        v = sorted(v, key=len, reverse=True)
        kws[y] = v
    return kws

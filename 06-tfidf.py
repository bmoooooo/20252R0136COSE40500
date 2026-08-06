import math
from collections import Counter

def compute_tfidf(documents):
    tfidf = []
    N = len(documents)

    df = Counter()
    for doc in documents:
        for word in set(doc):
            df[word] += 1

    for doc in documents:
        tf = Counter(doc)
        doc_tfidf = {}
        for word, freq in tf.items():
            idf = math.log(N / (df[word] + 1))
            doc_tfidf[word] = freq * idf
        tfidf.append(doc_tfidf)

    return tfidf

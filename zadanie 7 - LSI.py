import numpy as np
import string

def tokenizacja_tekstu(doc):
    return doc.translate(str.maketrans('', '', string.punctuation)).lower().split()

def policz_podobienstwo_cosinus(wektor_zapytania, wektor_dokumentu):
    dot_product = np.dot(wektor_zapytania, wektor_dokumentu)
    dlugosc_q = np.linalg.norm(wektor_zapytania)
    dlugosc_d = np.linalg.norm(wektor_dokumentu)
    cosinus = dot_product / (dlugosc_q * dlugosc_d + 1e-9) 
    return round(cosinus, 2)

def lsi(documents, query, k):
    terms = []
    for doc in documents + [query]:
        for term in tokenizacja_tekstu(doc):
            terms.append(term)

    terms = list(set(terms))

    n = len(documents)
    macierz_term_dokument = np.zeros((len(terms), n))

    for i, doc in enumerate(documents):
        term_occurrences = [1 if term in tokenizacja_tekstu(doc) else 0 for term in terms]
        macierz_term_dokument[:, i] = term_occurrences

    U, s, Vt = np.linalg.svd(macierz_term_dokument, full_matrices=False)

    Sr = np.diag(s[:k])
    Vk = Vt[:k, :]
    Ck = Sr.dot(Vk)

    q = np.array([1 if term in tokenizacja_tekstu(query) else 0 for term in terms])
    Sk_1 = np.linalg.inv(Sr)
    UkT = U.T[:k, :]
    qk = Sk_1.dot(UkT).dot(q)

    podobienstwa = [policz_podobienstwo_cosinus(qk, wektor_dokumentu) for wektor_dokumentu in Ck.T]
    return podobienstwa

n = int(input())
documents = [input() for i in range(n)]
query = input()
k = int(input())

podobienstwa = lsi(documents, query, k)

print(podobienstwa)
import numpy as np
import string
import re

def preprocess_document(doc):
    doc_tokens = doc.translate(str.maketrans('', '', string.punctuation)).lower().split()
    return doc_tokens

def calculate_cosine_similarity(question_vector, document_vector):
    iloczyn = np.dot(question_vector, document_vector)
    suma_squer = np.linalg.norm(question_vector) * np.linalg.norm(document_vector)

    if suma_squer == 0:
        return 0.0

    cosine = iloczyn / suma_squer
    return cosine

def lsi(documents, query, k):
    all_text = documents + [query]
    terms = list(set([term for doc in all_text for term in preprocess_document(doc)]))
    n = len(documents)
    term_document_matrix = np.zeros((len(terms), n))

    for i, doc in enumerate(documents):
        doc_tokens = preprocess_document(doc)
        for j, term in enumerate(terms):
            term_document_matrix[j, i] = doc_tokens.count(term)

    print("Term-Doc Incidence Matrix:")
    print(term_document_matrix)

    U, s, Vt = np.linalg.svd(term_document_matrix, full_matrices=False)

    Sr = np.diag(s[:k])
    Vk = Vt[:k, :]
    Ck = Sr.dot(Vk)

    q = np.array([1 if term in preprocess_document(query) else 0 for term in terms])
    Sk_1 = np.linalg.inv(Sr)
    UkT = U.T[:k, :]
    qk = Sk_1.dot(UkT).dot(q)

    similarities = [calculate_cosine_similarity(qk, document_vector) for document_vector in Ck.T]

    return similarities

n = int(input("Podaj liczbę dokumentów: "))
documents = [preprocess_document(input(f"Podaj dokument {i+1}: ")) for i in range(n)]
query = input("Podaj zapytanie: ")
k = int(input("Podaj liczbę wymiarów po zredukowaniu (k): "))

similarities = lsi(documents, query, k)

print("Similarities:", similarities)

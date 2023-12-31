import math
import string

def przetworz_dokument(doc):
    return doc.translate(str.maketrans('', '', string.punctuation))

def oblicz_podobienstwo(dokumenty, lista_query):
    wszystkie_slowa = []
    tf_dokumentow = []

    for doc in dokumenty:
        przetworzony_doc = przetworz_dokument(doc)
        slowa = przetworzony_doc.lower().split()
        wszystkie_slowa.extend(set(slowa))

        liczba_slow = len(slowa)
        tf = {}

        for slowo in set(slowa):
            czestosc_slowa = slowa.count(slowo)
            tf[slowo] = czestosc_slowa / liczba_slow

        max_tf = max(tf.values())

        for slowo in set(slowa):
            tf[slowo] = tf[slowo] / max_tf

        tf_dokumentow.append(tf)

    unikalne_slowa = set(wszystkie_slowa)
    slownik_idf = {}

    for slowo in unikalne_slowa:
        slownik_idf[slowo] = math.log10(len(dokumenty) / wszystkie_slowa.count(slowo))

    tfidf_tablica = []

    for tf in tf_dokumentow:
        tfidf_dokument = {slowo: tf[slowo] * slownik_idf[slowo] for slowo in tf}
        tfidf_tablica.append(tfidf_dokument)

    dlugosc_query = len(lista_query)

    for tfidf_dokument in tfidf_tablica:
        iloczyn = sum(tfidf_dokument[slowo] for slowo in lista_query if slowo in tfidf_dokument)
        suma_kwadratow = sum(tfidf_dokument[slowo]**2 for slowo in tfidf_dokument if slowo in lista_query)

        dice = round(iloczyn * 2 / (dlugosc_query * suma_kwadratow), 2)
        jaccard = round(iloczyn / (dlugosc_query + suma_kwadratow - iloczyn), 2)
        cosinus = round(iloczyn / (math.sqrt(dlugosc_query) * math.sqrt(suma_kwadratow)), 2)
        iloczyn = round(iloczyn, 2)

        wynik = [iloczyn, dice, jaccard, cosinus]
        print(wynik)

liczba_dokumentow = int(input())
dokumenty = []
for i in range(liczba_dokumentow):
    doc = input()
    dokumenty.append(doc)

query_input = input()
lista_query = query_input.lower().split()

oblicz_podobienstwo(dokumenty, lista_query)

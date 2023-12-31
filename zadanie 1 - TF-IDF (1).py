# tego zadania nie zrobiłyśmy, ale tutaj jest fragment kodu z zad 5, który oblicza TF-IDF. Jak coś odsyłam do zad 5
import math
import string

n = int(input())

dokumenty = []

for i in range(n):
    dok = input()
    dok = dok.translate(str.maketrans('', '', string.punctuation))
    dokumenty.append(dok)

print(dokumenty)

question = input()
question_list = question.lower().split()
question_length = len(question_list)

dok_tfs = []
wszytkie_slowa = []

# tf cout of word in text / number of world in text
for dok in dokumenty:
    # obliczyc tf-idf dla dla slowa w dok

    # tokenizacja i to lower case
    lista_slow = dok.lower().split()
    lista_unikalnych_slow = set(lista_slow)

    for unikat in lista_unikalnych_slow:
        wszytkie_slowa.append(unikat)

    liczba_slow = len(lista_slow)

    tf = {}

    for slowo in lista_unikalnych_slow:
        ile_powtorzen = lista_slow.count(slowo)
        tf[slowo] = ile_powtorzen

    max_in_tf = max(tf.values())

    for slowo in lista_unikalnych_slow:
        tf[slowo] = tf[slowo] / max_in_tf

    dok_tfs.append(tf)

# usuwamy powtorzenia
unikalne_wszytkie_slowa = set(wszytkie_slowa)

# idf log (ile dokumenow / w ilu dokumentach)

slownik_idf = {}

for slowo in unikalne_wszytkie_slowa:
    slownik_idf[slowo] = math.log10(n / wszytkie_slowa.count(slowo))

tablica = []

for tf in dok_tfs:
    mini_tablica = {}
    for slowo in tf:
        mini_tablica[slowo] = tf[slowo] * slownik_idf[slowo]
    tablica.append(mini_tablica)
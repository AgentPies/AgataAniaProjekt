n = int(input("Podaj liczbę wierszy: "))
text = []

for i in range(n):
    verse = input("Wpisz wiersze: ").strip().lower()
    text.append(verse)

m = int(input("Podaj liczbę słów do zliczenia: "))
words = []

for i in range(m):
    word = input("Podaj słowa, które mają być zliczone: ").strip()  
    words.append(word)

results = []

for word in words:
    word_results = []

    for i, verse in enumerate(text):
        count = verse.count(word)
        if count > 0:
            word_results.append((i, count))

    if word_results:
        word_results.sort(key=lambda x: (-x[1], x[0]))
        results.append(word_results)

for word_result in results:
    indexes = [index for index, _ in word_result]
    print(indexes)
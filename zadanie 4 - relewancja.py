def metryki(wyniki_wyszukiwania, oceny_relewancji):
    precyzja_lista = []
    wzgledna_pelnosc_lista = []
    f2_lista = []
    srednia_precyzja_lista = []

    for i in range(len(wyniki_wyszukiwania)):
        true = sum([1 for id_dokumentu in wyniki_wyszukiwania[i] if oceny_relewancji[id_dokumentu] == 1])
        false = len(wyniki_wyszukiwania[i]) - true

        precyzja = true / (true + false) if (true + false) > 0 else 0
        wzgledna_pelnosc = true / sum(oceny_relewancji) if sum(oceny_relewancji) > 0 else 0
        f2 = (1 + 2) * (precyzja * wzgledna_pelnosc) / ((2 * precyzja) + wzgledna_pelnosc) if (precyzja + wzgledna_pelnosc) > 0 else 0.0

        precyzja_lista.append(round(precyzja, 2))
        wzgledna_pelnosc_lista.append(round(wzgledna_pelnosc, 2))
        f2_lista.append(round(f2, 2))

        relewancja_wynikow = [oceny_relewancji[id_dokumentu] for id_dokumentu in wyniki_wyszukiwania[i]]
        relewancja_na_pozycji = [sum(relewancja_wynikow[:j+1]) / (j+1) for j in range(len(relewancja_wynikow))]
        relewancja_ostateczna = [relewancja_wynikow[j] * relewancja_na_pozycji[j] for j in range(len(relewancja_wynikow))]

        R = sum(oceny_relewancji)
        srednia_precyzja = sum(relewancja_ostateczna) / R if R > 0 else 0.0
        srednia_precyzja_lista.append(round(srednia_precyzja, 2))

    return precyzja_lista, wzgledna_pelnosc_lista, f2_lista, srednia_precyzja_lista

def main():
    n = int(input())
    wyniki_wyszukiwania = []
    oceny_relewancji = []

    for i in range(n):
        wynik_wyszukiwania = list(map(int, input().strip().split()))
        wyniki_wyszukiwania.append(wynik_wyszukiwania)

    oceny_relewancji = list(map(int, input().strip().split()))

    precyzja_lista, wzgledna_pelnosc_lista, f2_lista, srednia_precyzja_lista = metryki(wyniki_wyszukiwania, oceny_relewancji)

    for i in range(n):
        wyniki = [precyzja_lista[i], wzgledna_pelnosc_lista[i], f2_lista[i], srednia_precyzja_lista[i]]
        print(wyniki)

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup

def pobierz_informacje_o_artykule(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    bodyContent = soup.find('div', attrs={'id' : 'mw-content-text'})
    nazwy_artykulow = []
    for link in bodyContent.find_all('a', href=True):
        link_href = link['href']
        if link_href.startswith('/wiki/') and ':' not in link_href:
            nazwy_artykulow.append(link.text.strip())
            if len(nazwy_artykulow) == 6:
                break

    adresy_url_obrazkow = []
    for img in bodyContent.find_all('img', src=True):
        adresy_url_obrazkow.append(img['src'])
        if len(adresy_url_obrazkow) == 4:
            break

    adresy_url_zrodel = []
    for ref in bodyContent.find_all('a', href=True):
        href = ref['href']
        if href.startswith('http'):
            adresy_url_zrodel.append(href)
            if len(adresy_url_zrodel) == 3:
                break

    kategorie = []
    for kategoria in soup.find_all('div', {'class': 'mw-normal-catlinks'}):
        for cat_link in kategoria.find_all('a', href=True):
            kategorie.append(cat_link.text.strip())
            if len(kategorie) == 3:
                break

    return nazwy_artykulow[1:], adresy_url_obrazkow[1:], adresy_url_zrodel, kategorie

def main():
    kategoria = input("Podaj nazwę kategorii na Wikipedii: ")
    base_url = 'https://pl.wikipedia.org/wiki/'
    kategoria_url = base_url + 'Kategoria:' + kategoria.replace(' ', '_')
    
    response = requests.get(kategoria_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    adresy_url_artykulow = []
    nazwy_artykulow = []
    mwKategoria = soup.find('div', attrs={'class' : 'mw-category-generated'})
    for link in mwKategoria.find_all('a', href=True):
        link_href = link['href']
        if link_href.startswith('/wiki/') and ':' not in link_href:
            adresy_url_artykulow.append(base_url + link_href[6:])
            nazwy_artykulow.append(link.text.strip())
            if len(adresy_url_artykulow) == 2:
                break

    for url, name in zip(adresy_url_artykulow, nazwy_artykulow):
        print(name)
        informacje_o_artykule = pobierz_informacje_o_artykule(url)
        for info in informacje_o_artykule:
            print(' | '.join(info))
        print()

if __name__ == '__main__':
    main()
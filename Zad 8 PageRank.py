import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import numpy as np


# get all the links from the page
def get_links(base_url, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True)]
    return links


# Page Rank
def page_rank(graph, damping_factor=0.85, iterations=20, tolerance=0.0000001):
    nodes = list(graph.keys())
    num_nodes = len(nodes)

    macierz_przejscia = np.zeros((num_nodes, num_nodes))

    for i, node in enumerate(nodes):
        neighbors = graph[node]
        if neighbors:
            for neighbor in neighbors:
                j = nodes.index(neighbor)
                macierz_przejscia[i, j] = 1 / len(neighbors)

    for i in range(num_nodes):
        if np.sum(macierz_przejscia[i, :]) == 0:
            macierz_przejscia[i, :] = 1 / num_nodes

    # normalizacja
    sumy_wierszy = macierz_przejscia.sum(axis=1)
    sumy_wierszy_z_wymiarami = sumy_wierszy.reshape(-1, 1)
    macierz_przejscia = macierz_przejscia / sumy_wierszy_z_wymiarami

    macierz_przejscia = damping_factor * macierz_przejscia + (1 - damping_factor) / num_nodes

    pg_values = np.ones(num_nodes) / num_nodes

    for _ in range(iterations):
        prev_pg_values = pg_values.copy()
        pg_values = np.dot(macierz_przejscia.T, pg_values)

        if np.linalg.norm(pg_values - prev_pg_values, 1) < tolerance:
            break

    return dict(zip(nodes, pg_values))


# main function, graph construction
def calculations(url_to_crawl):
    graph = {}
    urls_visited = set()

    def crawl(url):
        if url not in urls_visited:
            urls_visited.add(url)
            links = get_links(url_to_crawl, url)

            if url not in graph:
                graph[url] = []

            for link in links:
                graph[url].append(link)
                crawl(link)

    crawl(url)
    pg_values = page_rank(graph)

    sorted_results = [pg_values[url] for url in sorted(pg_values.keys())]
    return sorted_results


# run
url = input()
results = [round(value, 4) for value in calculations(url)]
print(results)
import requests, re

response = requests.request(url='https://en.wikipedia.org/wiki/Lists_of_films', method='GET')
table = re.findall(r'<table class="wikitable"(.*?)</table>', response.text, re.DOTALL)[0]
rows = re.findall(r'<tr>(.*?)</tr>', table, re.DOTALL)[1:]
links = [re.findall(r'<a href="(.*?)"', row, re.DOTALL) for row in rows]

# for link in links:
response = requests.request(url='https://en.wikipedia.org' + links[0][0], method='GET')
movie_links = re.findall(r'<i><a href="(.*?)"', response.text, re.DOTALL)
# for movie_link in movie_links:
print('https://en.wikipedia.org' + movie_links[0])
response = requests.request(url='https://en.wikipedia.org' + movie_links[0], method='GET')
info_box = re.findall(r'<table class="infobox vevent"(.*?)</table>', response.text, re.DOTALL)[0]
description = re.findall(r'<p>(.*?)</p>', response.text, re.DOTALL)[0]
# print(description)
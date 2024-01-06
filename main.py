import requests, re, json

with open('data.json', 'w') as json_file:
    json_file.write('[')
    
response = requests.request(url='https://en.wikipedia.org/wiki/Lists_of_films', method='GET')
table = re.findall(r'<table class="wikitable"(.*?)</table>', response.text, re.DOTALL)
rows = re.findall(r'<tr>(.*?)</tr>', table[0], re.DOTALL)
links = []
for row in rows:
    links = links + re.findall(r'<a href="(.*?)"', row, re.DOTALL)
    
for link in links:
    response = requests.request(url='https://en.wikipedia.org' + link, method='GET')
    movie_links = re.findall(r'<i><a href="(.*?)"', response.text, re.DOTALL)
    for movie_link in movie_links:
        try:
            response = requests.request(url='https://en.wikipedia.org' + movie_link, method='GET')
            info_box = re.findall(r'<table class="infobox vevent"(.*?)</table>', response.text, re.DOTALL)
            
            title = re.findall(r'<th colspan="2" class="infobox-above summary" .*?>(.*?)<\/th>', info_box[0])
            
            director = re.findall(r'<th .*?>Directed by<\/th><td .*?><a .*?>(.*?)<\/a>', info_box[0])
            
            cast = re.findall(r'<th .*?>Starring<\/th><td .*?>(.*?)<\/td>', info_box[0])
            cast = re.sub(r'<.*?>', '.', cast[0])
            cast = cast.split('.')
            cast = [i for i in cast if i and i != ' ']

            music = re.findall(r'<th .*?>Music by<\/th><td .*?><a .*?>(.*?)<\/a>', info_box[0])
            
            country = re.findall(r'<tr><th .*?>Country<\/th><td class="infobox-data">(.*?)<\/td><\/tr>', info_box[0])
            country = re.sub(r'<.*?>', '', country[0])
            
            release_date = re.findall(r'\b(\d{4}-\d{2}-\d{2})\b', info_box[0])
            year, month, day = release_date[0].split('-')
            
            duration = re.findall(r'<tr><th .*?>Running time<\/div><\/th><td class="infobox-data">(.*?) minutes', info_box[0])
            
            description_html = re.findall(r'<p>(.*?)</p>', response.text, re.DOTALL)
            description = re.sub(r'<.*?>', '', description_html[0])
            description = re.sub(r'&#.*?;', '', description)
            
            JSON = {
                'title': title[0],
                'director': director[0],
                'music': music[0],
                'cast': cast,
                'country': country,
                'release_date': {
                    'year': year,
                    'month': month,
                    'day': day
                },
                'duration': duration[0],
                'description': description,
                'description_html': description_html[0]
            }
            json.dump(JSON, open('data.json', 'a'), indent=4, separators=(',', ': '))
            with open('data.json', 'a') as json_file:
                json_file.write(',\n')

        except IndexError:
            pass
        
with open('data.json', 'rb+') as json_file:
    json_file.seek(-1, 2)
    json_file.truncate()
    json_file.write(']')
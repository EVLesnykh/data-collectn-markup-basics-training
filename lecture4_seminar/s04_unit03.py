# Импорт необходимых библиотек
import requests
from lxml import html
from pymongo import MongoClient
import time

# Определение целевого URL
url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1"

# Отправка HTTP GET запроса на целевой URL с пользовательским заголовком User-Agent
response = requests.get(url, headers = {
   'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# Парсинг HTML-содержимого ответа с помощью библиотеки lxml
tree = html.fromstring(response.content)
# Использование выражения XPath для выбора всех строк таблицы в пределах таблицы с классом 'records-table'
table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")

data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    data.append({
        'rank': columns[0].strip(),
        'mark': columns[1].strip(),
        'competitor': row.xpath(".//td[3]/a/text()")[0].strip(),
        'dob': columns[4].strip(),
        'nat': columns[6].strip(),
        'pos': columns[7].strip(),
        'venue': columns[8].strip(),
        'date': columns[9].strip(),
        'resultscore': columns[10].strip()
    })

print(data)
# Импорт необходимых библиотек
import requests
from lxml import html
from pymongo import MongoClient
import time
import pandas as pd

# Определение целевого URL
url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1"

# Отправка HTTP GET запроса на целевой URL с пользовательским заголовком User-Agent
response = requests.get(url, headers = {
   'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# Парсинг HTML-содержимого ответа с помощью библиотеки lxml
tree = html.fromstring(response.content)
print(tree)

# Использование выражения XPath для выбора всех строк таблицы в пределах таблицы с классом 'records-table'
table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")

data_list =[]
for rows in table_rows:
  data ={}
  columns = rows.xpath(".//td/text()")
  data["rank"] = int(columns[0].strip())
  data["mark"] = float(columns[1].strip())
  data["WIND"] = columns[2].strip() if columns[2].strip else "0"
  data["competitor"] = rows.xpath(".//td[4]/a/text()")[0].strip()
  data["dob"] = columns[5].strip()
  data["nat"] = columns[6].strip()
  data["pos"] = columns[7].strip()
  data["venue"] = columns[8].strip()
  data["date"] = columns[9].strip()
  data["resultscore"] = int(columns[11].strip())
  data_list.append(data)
for data in data_list:
  print(data)

# Теперь импортируем данные  в базу данных, например в pandas
df = pd.DataFrame(data_list)
print(df)
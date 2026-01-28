# Задание 3

# - Создайте сценарий Python, который запрашивает данные из Foursquare API с помощью библиотеки requests.
# - Сценарий должен предложить пользователю ввести название города.
# - Затем сценарий должен отправить запрос в Foursquare API для поиска ресторанов в указанном городе.
# - Сценарий должен обработать ответ API и извлечь название и адрес каждого ресторана.
# - Скрипт должен вывести название и адрес каждого ресторана в консоль.

# Требования:
# Использовать API Foursquare для получения данных.
# Использовать библиотеку requests для отправки запросов API
# Использовать библиотеку json для обработки ответа API.
# Запросить у пользователя название города
# Извлечь и вывести название и адрес каждого ресторана из ответа API.

import requests
import json

# Ваши учетные данные API
client_id = "__"
client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"
city=input('Введите название города: ')
params={
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": "cafe"
}
headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue["location"]["address"])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

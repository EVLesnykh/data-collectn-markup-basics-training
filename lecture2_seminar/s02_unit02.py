import requests
from bs4 import BeautifulSoup

# Запрос веб-страницы
url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab'
response = requests.get(url)

# Парсинг HTML-содержимого веб-страницы с помощью Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Вывод HTML-содержимого веб-страницы
print(soup.prettify())

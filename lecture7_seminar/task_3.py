# Импорт необходимых библиотек
from selenium import webdriver  # Для управления веб-драйвером
from selenium.webdriver.chrome.options import Options  # Для настройки опций Chrome
# Для определения способа поиска элементов
from selenium.webdriver.common.by import By
# Для ожидания загрузки элементов
from selenium.webdriver.support.ui import WebDriverWait
# Для ожидания конкретных условий
from selenium.webdriver.support import expected_conditions as EC
import time  # Для задержки выполнения
import json  # Для работы с JSON

# Настройка User-Agent для WebDriver
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
chrome_options = Options()
# Установка User-Agent в опции браузера
chrome_options.add_argument(f'user-agent={user_agent}')

# Инициализация драйвера Chrome с заданными опциями
driver = webdriver.Chrome(options=chrome_options)

# URL канала YouTube для скрапинга
youtube_channel_url = "https://www.youtube.com/@progliveru/videos"

try:
    # Переход по указанному URL
    driver.get(youtube_channel_url)

# Ожидание загрузки страницы
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body")))

# Скроллинг страницы для загрузки контента
    page_height = driver.execute_script(
    "return document.documentElement.scrollHeight")
    scroll_pause_time = 2
    while True:
    # Прокрутка до конца страницы
        driver.execute_script(
    "window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(scroll_pause_time)
# Проверка, достигнут ли конец страницы
        new_height = driver.execute_script(
    "return document.documentElement.scrollHeight")
        if new_height == page_height:
           break
        page_height = new_height

# Xpath для заголовков видео и метаданных
    video_titles_xpath = "//*[@id='video-title-link']"
    metadata_xpath = "//div[@id='metadata-line']/span[1]"

# Поиск элементов по Xpath
    video_titles = driver.find_elements(By.XPATH, video_titles_xpath)
    metadata_elements = driver.find_elements(By.XPATH, metadata_xpath)

# Сбор данных о видео
    video_data = {}
    for i in range(min(len(video_titles), len(metadata_elements))):
        title = video_titles[i].text
        metadata_text = metadata_elements[i].text

# Разделение метаданных на просмотры и время публикации
        if "•" in metadata_text:
            views, time_ago = metadata_text.split("•")
        else:
            views = metadata_text
            time_ago = "Неизвестно"

# Сохранение данных в словарь
        video_data[title] = {"views": views.strip(), "published": time_ago.strip()}

# Запись данных в файл JSON
    with open('video_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(video_data, json_file, ensure_ascii=False, indent=4)

# Вывод сообщения об успешном сохранении
    print("Данные сохранены в файл 'video_data.json'")

except Exception as e:
    # Вывод сообщения об ошибке
    print("Произошла ошибка:", e)

finally:
    # Закрытие драйвера браузера
    driver.quit()

"""
Подробные объяснения:
- Данный скрипт использует Selenium, библиотеку для автоматизации действий веб-браузера.
- С помощью WebDriver Chrome скрипт открывает страницу YouTube-канала и скроллит её, чтобы загрузить данные о всех видео.
- Скрипт ищет заголовки и метаданные каждого видео на странице, используя XPath.
- Извлеченные данные (название видео, количество просмотров, дата публикации) сохраняются в формате JSON.
- Используется обработка исключений для управления ошибками во время выполнения скрипта.
- Скрипт завершает работу, корректно закрывая драйвер браузера.
"""


# ВЕРСИЯ С КОММЕНТАРИЯМИ

"""
# Импорт необходимых библиотек
from selenium import webdriver # Для управления веб-драйвером
from selenium.webdriver.chrome.options import Options # Для настройки опций Chrome
from selenium.webdriver.common.by import By # Для определения способа поиска элементов
from selenium.webdriver.support.ui import WebDriverWait # Для ожидания загрузки элементов
from selenium.webdriver.support import expected_conditions as EC # Для ожидания конкретных условий
import time # Для задержки выполнения
import json # Для работы с JSON

# Настройка User-Agent для WebDriver
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}') # Установка User-Agent в опции браузера

# Инициализация драйвера Chrome с заданными опциями
driver = webdriver.Chrome(options=chrome_options)

# URL канала YouTube для скрапинга
youtube_channel_url = "https://www.youtube.com/@progliveru/videos"

try:
# Переход по указанному URL
driver.get(youtube_channel_url)

# Ожидание загрузки страницы
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Скроллинг страницы для загрузки контента
page_height = driver.execute_script("return document.documentElement.scrollHeight")
scroll_pause_time = 2
while True:
# Прокрутка до конца страницы
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
time.sleep(scroll_pause_time)
# Проверка, достигнут ли конец страницы
new_height = driver.execute_script("return document.documentElement.scrollHeight")
if new_height == page_height:
break
page_height = new_height

# Xpath для заголовков видео и метаданных
video_titles_xpath = "//*[@id='video-title-link']"
metadata_xpath = "//div[@id='metadata-line']/span[1]"

# Поиск элементов по Xpath
video_titles = driver.find_elements(By.XPATH, video_titles_xpath)
metadata_elements = driver.find_elements(By.XPATH, metadata_xpath)

# Сбор данных о видео
video_data = {}
for i in range(min(len(video_titles), len(metadata_elements))):
title = video_titles[i].text
metadata_text = metadata_elements[i].text

# Разделение метаданных на просмотры и время публикации
if "•" in metadata_text:
views, time_ago = metadata_text.split("•")
else:
views = metadata_text
time_ago = "Неизвестно"

# Сохранение данных в словарь
video_data[title] = {"views": views.strip(), "published": time_ago.strip()}

# Запись данных в файл JSON
with open('video_data.json', 'w', encoding='utf-8') as json_file:
json.dump(video_data, json_file, ensure_ascii=False, indent=4)

# Вывод сообщения об успешном сохранении
print("Данные сохранены в файл 'video_data.json'")

except Exception as e:
# Вывод сообщения об ошибке
print("Произошла ошибка:", e)

finally:
# Закрытие драйвера браузера
driver.quit()
"""
"""
Подробные объяснения:
- Данный скрипт использует Selenium, библиотеку для автоматизации действий веб-браузера.
- С помощью WebDriver Chrome скрипт открывает страницу YouTube-канала и скроллит её, чтобы загрузить данные о всех видео.
- Скрипт ищет заголовки и метаданные каждого видео на странице, используя XPath.
- Извлеченные данные (название видео, количество просмотров, дата публикации) сохраняются в формате JSON.
- Используется обработка исключений для управления ошибками во время выполнения скрипта.
- Скрипт завершает работу, корректно закрывая драйвер браузера.
"""

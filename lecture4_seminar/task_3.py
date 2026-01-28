# Импорт необходимых библиотек
import requests # Библиотека для выполнения HTTP-запросов
from lxml import html # Библиотека для парсинга HTML
from pymongo import MongoClient # Библиотека для работы с MongoDB
import time # Библиотека для управления временем

# Функция для скрейпинга табличных данных с одной страницы
def scrape_page_data(url):
    # Отправляем GET-запрос к указанному URL и получаем ответ
    response = requests.get(url)

    # Создаем объект дерева HTML из содержимого ответа
    tree = html.fromstring(response.content)

    # Используем XPath для выбора всех строк таблицы с классом 'records-table'
    table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")

    # Создаем пустой список для хранения данных
    data = []

    # Итерируемся по строкам таблицы и извлекаем необходимые данные
    for row in table_rows:
        # Используем XPath, чтобы извлечь текст из ячеек таблицы
        columns = row.xpath(".//td/text()")
        data.append({
            'rank': columns[0].strip(), # Извлекаем и очищаем значение столбца 'rank'
            'mark': columns[1].strip(), # Извлекаем и очищаем значение столбца 'mark'
            'WIND': columns[2].strip() if columns[2].strip else "0",
            'competitor': row.xpath(".//td[4]/a/text()")[0].strip(), # Извлекаем и очищаем значение столбца 'competitor'
            'dob': columns[5].strip(), # Извлекаем и очищаем значение столбца 'dob'
            'nat': columns[6].strip(), # Извлекаем и очищаем значение столбца 'nat'
            'pos': columns[7].strip(), # Извлекаем и очищаем значение столбца 'pos'
            'venue': columns[8].strip(), # Извлекаем и очищаем значение столбца 'venue'
            'date': columns[9].strip(), # Извлекаем и очищаем значение столбца 'date'
            'resultscore': int(columns[11].strip()) # Извлекаем и очищаем значение столбца 'resultscore'
        })
    return data

# Функция для сохранения данных в MongoDB
def save_data_to_mongo(data):
    # Устанавливаем соединение с локальной MongoDB на порту 27017
    client = MongoClient('localhost', 27017)

    # Выбираем базу данных 'world_athletics'
    db = client['world_athletics']

    # Выбираем коллекцию 'sprints_60_metres'
    collection = db['sprints_60_metres']

    # Вставляем множество документов (записей) в коллекцию
    collection.insert_many(data)

# Основная функция
def main():
    # Базовый URL, откуда будут скрейпиться данные с разных страниц
    base_url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page="

    # Итерируемся по страницам (от 1 до 6)
    for page in range(1, 7):
        print(f"Scraping page {page}...") # Выводим информацию о текущей странице
        url = base_url + str(page) # Формируем полный URL для текущей страницы
        data = scrape_page_data(url) # Вызываем функцию для скрейпинга данных
        save_data_to_mongo(data) # Вызываем функцию для сохранения данных в MongoDB
        time.sleep(5) # Приостанавливаем выполнение программы на 5 секунд для осторожности

# Проверяем, что код выполняется как самостоятельная программа, а не импортируется как модуль
if __name__ == "__main__":
    main()
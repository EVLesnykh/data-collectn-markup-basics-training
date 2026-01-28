# Задание 1
# - Создайте проект Scrapy и паука для скрейпинга только названий стран из таблицы.
# - Добавьте User Agent.
# - Реализуйте метод извлечения данных с помощью селекторов CSS или XPath и получения элементов Scrapy.
# - Сохраните данные в JSON-файл.

# Паук должен записывать извлеченные данные в словарь.

# - Модифицируйте предыдущий сценарий, чтобы получить дополнительные данные из столбцов таблицы: 
# Membership within the UN, Sovereignty dispute information, Country status.
# - В методе parse выполните итерации по строкам стран в таблице (wikitable).
# - Извлеките из таблицы требуемые данные.
# - Сохраните данные в JSON-файл. Запустите паука с помощью команды:
#  scrapy crawl countries_spider -o output.json, чтобы сохранить собранные данные в JSON-файл.

# Если какая-либо извлеченная информация отсутствует, установите для соответствующего словаря значение None.

import scrapy


class CountriesSpiderSpider(scrapy.Spider):
    name = "countries_spider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_sovereign_states"]

    def parse(self, response):
        for country in response.css('table.wikitable.sortable tbody tr'):
            name = country.css('td:nth-child(1) b a::text').get()
            if name:
                yield{
                    'name' : name
                }

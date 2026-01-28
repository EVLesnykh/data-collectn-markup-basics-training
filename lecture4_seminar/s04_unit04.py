import requests
from lxml import html
from pymongo import MongoClient
import time

# Функция для скрейпинга табличных данных с одной страницы
def scrape_page_data(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
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
    return data

# Функция для сохранения данных в MongoDB
def save_data_to_mongo(data):
    client = MongoClient('localhost', 27017)
    db = client['world_athletics']
    collection = db['sprints_60_metres']
    collection.insert_many(data)

# Main function
def main():
    base_url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page="

    for page in range(1, 7):
        print(f"Scraping page {page}...")
        url = base_url + str(page)
        data = scrape_page_data(url)
        save_data_to_mongo(data)
        time.sleep(5)

if __name__ == "__main__":
    main()

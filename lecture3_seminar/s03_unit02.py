from pymongo import MongoClient
import json

# создание экземпляра клиента
client = MongoClient()

# подключение к базе данных и коллекции
db = client['town_cary']
collection = db['crashes']

# вывод первой записи в коллекции
all_docs = collection.find()
first_doc = all_docs[0]

# Вывод объекта JSON
pretty_json = json.dumps(first_doc, indent=4, default=str)
print(pretty_json)

# Получение количества документов в коллекции с помощью функции count_documents()
count = collection.count_documents({})
print(f'Число записей в базе данных: {count}')

# фильтрация документов по критериям
query = {"properties.fatalities": "Yes"}
print(f"Количество документов c категорией fatalities: {collection.count_documents(query)}")

# Использование проекции
query = {"properties.fatalities": "Yes"}
projection = {"properties.lightcond": 1, "properties.weather": 1, "_id": 0}
proj_docs = collection.find(query, projection)
for doc in proj_docs:
    print(doc)

# Использование оператора $lt и $gte
query = {"properties.month": {"$lt": "6"}}
print(f"Количество документов c категорией month < 6: {collection.count_documents(query)}")
query = {"properties.month": {"$gte": "6"}}
print(f"Количество документов c категорией month >= 6: {collection.count_documents(query)}")

# Использование оператора $regex
query = {"properties.weather": {"$regex": "rain", "$options": "i"}}
print(f"Количество документов, содержащих 'rain': {collection.count_documents(query)}")

# Использование оператора $in
query = {"properties.rdclass": {"$in": ["US ROUTE", "STATE SECONDARY ROUTE"]}}
print(f"Количество документов в категории rdclass: {collection.count_documents(query)}")

# Использование оператора $all
query = {"properties.rdconfigur": {"$all": ["TWO-WAY", "DIVIDED"]}}
print(f"Количество документов в категории rdconfigur: {collection.count_documents(query)}")

# Использование оператора $ne
query = {"properties.rdcondition" : {"$ne": "DRY"}}
print(f"Количество документов в категории rdcondition: {collection.count_documents(query)}")

query = {"properties.fatalities": "Yes"}
projection = {"properties.lightcond": 1, "properties.weather": 1, "_id": 0}
proj_docs = collection.find(query, projection)
for doc in proj_docs:
    print(doc)
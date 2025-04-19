from pymongo import MongoClient
import json

# Подключение к локальному серверу MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['books_db']
collection = db['items']

# Чтение данных из файла
with open('books_data.json', 'r', encoding='utf-8', errors='ignore') as file:
    data = json.load(file)

# Вставка данных
collection.insert_many(data)
print("Данные успешно загружены в MongoDB.")
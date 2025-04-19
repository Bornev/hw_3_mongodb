from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['books_db']
collection = db['items']

# 1. Получение всех документов
print("Все документы:")
all_docs = collection.find()
for doc in all_docs:
    print(doc)

# 2. Фильтрация (цена > 58)
print("\nДокументы с ценой больше 58:")
expensive_items = collection.find({"price": {"$gt": 58}})
for item in expensive_items:
    print(item)

# 3. Проекция (title и price)
print("\nТолько title и price:")
projection = collection.find({}, {"title": 1, "price": 1, "_id": 0})
for doc in projection:
    print(doc)

# 4. Подсчет (категория Fiction)
count = collection.count_documents({"category": "Fiction"})
print(f"\nКоличество книг в категории Fiction: {count}")

# 5. Агрегация (подсчет по категориям)
print("\nПодсчет по категориям:")
pipeline = [
    {"$group": {"_id": "$category", "count": {"$sum": 1}}}
]
result = collection.aggregate(pipeline)
for res in result:
    print(res)

# Дополнительно: фильтрация с $in
print("\nКатегории Fiction или Non-Fiction:")
specific_categories = collection.find({"category": {"$in": ["Fiction", "Non-Fiction"]}})
for item in specific_categories:
    print(item)

# Дополнительно: регулярное выражение
print("\nНазвания, начинающиеся с 'B':")
regex_query = collection.find({"title": {"$regex": "^B"}})
for item in regex_query:
    print(item)
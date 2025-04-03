import json
from pymongo import MongoClient
from pprint import pprint



client = MongoClient('localhost', 27017)
db = client['library']
books = db.books #create collections

# with open('books_data.json', 'r') as f:
#     data = json.load(f)
#
# for item in data:
#     books.insert_one(item)

# Счетчик общего количества книг
# count = books.count_documents({})
# print(f'Всего в базе данных {count} книг')
# print()
#

# # Поиск необходимой книги (при условии, что пользователь знает наизусть все книги в данной ДБ :)
# numOfBook = int(input('Введите порядковый номер книги: '))
# all_books = books.find()
# your_book = all_books[numOfBook - 1]
# print('Вот выбранная книга:')
# pprint(your_book)

# Фильтрация по выбранным параметрам
print(db.books.distinct('category'))

choosen_category = str(input('Выберите категорию из предложенных выше: '))
in_stock1,in_stock2 =  map(int, input('Введите значение через запятую: ').split(','))
filtred = {'$and':[{'in_stock': {'$gt': in_stock1,'$lt': in_stock2}}, {'category': choosen_category}]}
print(f'Кол-во книг по выбранным параметрам: {books.count_documents(filtred)}')
print()

# Проекция
projection = {'_id': 0,'title': 1, 'price': 1, 'in_stock': 1}
books_projection = books.find(filtred,projection)
for books in books_projection:
    print(books)

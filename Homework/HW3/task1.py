import json
from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *


client = MongoClient('localhost', 27017)
db = client['library']
# db2 = client['books']
books = db.books #create collections
# duplicates = db.duplicates

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

# Фильтрация по выбранному параметру
print(db.books.distinct('category'))
choosen_category = str(input('Выберите категорию из предложенных: '))
filtred = {'category' : choosen_category}
print(f'Кол-во книг в выбранной категории: {books.count_documents(filtred)}')




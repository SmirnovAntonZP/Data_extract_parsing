from lxml import html
import requests
import csv
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
url = 'https://www.cbr.ru'
response = requests.get(url + '/currency_base/daily/', headers = header)

tree = html.fromstring(response.content)
# Использование выражения XPath для выбора всех строк таблицы в пределах таблицы с классом 'data'
table_rows = tree.xpath("//table[@class='data']//tr")



new_list = []

for item in table_rows:
    list_item = item.xpath(".//td/text()")
    if len(list_item):
        currency = {}

        # Изменяем формат столбца 'код валюты' str->int
        try:
            currency['digital_code'] = int(list_item[0])
        except ValueError:
            currency['digital_code'] = None

        currency['letter code'] = list_item[1]

        # Изменяем формат столбца 'еденицы' str->int
        try:
            currency['units'] = int(list_item[2])
        except ValueError:
            currency['units'] = None

        currency['currency_name'] = list_item[3]

        # Изменяем формат столбца 'курс' str->float
        try:
            currency['rate'] = float(list_item[4].replace(',', '.'))
        except ValueError:
            currency['rate'] = None

        new_list.append(currency)

# Запись данных в csv-файл

CSV_FILE = 'currency.csv'

# Запись файла
with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f_write:
    fieldnames = ['digital_code', 'letter code', 'units', 'currency_name', 'rate']
    writer = csv.DictWriter(f_write, fieldnames=fieldnames, dialect='excel',
                            delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Записываем заголовки столбцов
    writer.writeheader()
    # Записываем все данные
    writer.writerows(new_list)

# Читаем наш CSV и преобразовывоем его в датафрем
data = pd.read_csv(CSV_FILE)
df = pd.DataFrame(data, columns=['digital_code', 'letter code', 'units', 'currency_name', 'rate'])
# Посмотрим инфу о датафрейме
df.info()
# Выведем курсы валют
df.head(100)
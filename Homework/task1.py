import json
import requests

url = "https://api.foursquare.com/v3/places/search"

headers = {
    "Authorization": "fsq30crRa1ZQAJVqYBVlkdgrwI+D3NTu+kaZUfGlmBGnpIk=",
    "accept": "application/json"
}

city = input("Введите название города: ")
place = input("Введите категорию заведения (кофейни, музеи, парки и т.д): ")

params = {
    "near": city,
    "query": place,
    "fields": "name,location,rating"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос")
    data = json.loads(response.text)
    items = data["results"]
    for item in sorted(items, key = lambda item: item['name']):
        print(f"{item['name']}, адрес: {item['location'].get('formatted_address', 'не определен') if item.get('location') else 'нет адреса'}, рейтинг {item.get('rating','не определен')}")
else:
    print("Запрос завершился ошибкой")
    print(response.status_code)
#
# import requests
# import json
#
# # Ваши учетные данные API
# CLIENT_ID = 'ZBTGA05DZIG1DKVHVULXWVCPACPKEOTBBL0CABLXGHX5QICL'
# CLIENT_SECRET = 'QXQAD4J00VVDQS2TOTGW1R4CINUPFPHRWWH5BSQCBMHBA40C'
#
# # # Конечная точка API
# endpoint = "https://api.foursquare.com/v3/places/search"
#
# # Определение параметров для запроса API
# city = input("Введите название города: ")
# category = input("Введите наименование категории: ")
#
# params = {
#     "client_id": CLIENT_ID,
#     "client_secret": CLIENT_SECRET,
#     "near": city,
#     "query": category
# }
#
# headers = {
#     "Accept": "application/json",
#     "Authorization": "fsq3X4ThjIBPvSGUlebP8R4CeQ5bdrGL/9gLVqlWzuCJmk8="
# }
#
# # Отправка запроса API и получение ответа
# response = requests.get(endpoint, params=params, headers=headers)
#
# # Проверка успешности запроса API
# if response.status_code == 200:
#     print("Успешный запрос. Вот что нашлось по вашему запосу:")
#     data = json.loads(response.text)
#     venues = data["results"]
#     for venue in venues:
#         print("Название:", venue["name"])
#         print("Адрес:", venue["location"]["address"])
#         print("\n")
# else:
#     print("Запрос неудадся с кодом состояния:", response.status_code)
#     print(response.text)
#
# # тренировка записи полученных данных в файл
# with open('response_data.json', 'w') as f:
#     json.dump(data, f)

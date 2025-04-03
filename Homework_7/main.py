# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Инициализация веб-драйвера
# service = Service('/path/to/chromedriver')  # Укажите путь к вашему chromedriver
# driver = webdriver.Chrome(service=service)
#
# # URL сайта, на который нужно перейти
# url = 'https://books.toscrape.com'
#
# # Открытие браузера и переход на страницу
# driver.get(url)
# time.sleep(2)  # Даем странице время на загрузку
#
# # Идентификация элементов HTML
# # Например, заголовки статей могут быть в элементе <h1>
# article_headers = driver.find_element(By.XPATH, '//ul/li/ul/li[1]/a')
#
# # Парсинг содержимого HTML с помощью BeautifulSoup
# from bs4 import BeautifulSoup
#
# # Преобразуем содержимое страницы в HTML
# html_content = driver.page_source
# soup = BeautifulSoup(html_content, "html.parser")
#
# # Извлечение заголовков статей
# article_titles = []
# for header in article_headers:
#     title = header.text
#     article_titles.append(title)
#
# # Пример вывода заголовков статей
# print("Заголовки статей:")
# for title in article_titles:
#     print("- ", title)
#
# # Закрытие браузера
# driver.quit()
#
#
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36")

chrome_options = Options()
chrome_options.add_argument(f'user_agent={user_agent}')

# Инициализация веб-драйвера
driver = webdriver.Chrome(options=chrome_options)

try:
    # Открытие сайта
    driver.get("https://books.toscrape.com")

    pause_time = 2
    # Переход в раздел Travel
    travel_link = driver.find_element(By.XPATH, '//ul/li/ul/li[1]/a')
    time.sleep(pause_time)
    travel_link.click()

    # Выполнение скроллинга страницы вниз
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
    time.sleep(pause_time)

    # Переход назад главную страницу
    travel_link = driver.find_element(By.XPATH, '//div[@class="col-sm-8 h1"]/a')
    travel_link.click()
    time.sleep(pause_time)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()

import requests
from bs4 import BeautifulSoup
import json

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

try:
    books_data = []

    for book in soup.find_all('h3'):
        title = book.a['title']
        book_url = book.a['href']
        full_book_url = f'https://books.toscrape.com/catalogue{book_url}'
        price = book.find_next('p', class_='price_color').text.strip()[2:]
        availability = book.find_next('p', class_='instock availability').text.strip()

        # Сохранение данных в виде словаря
        book_data = {
            'Title': title,
            'URL': full_book_url,
            'Price': price,
            'Availability': availability
        }

        books_data.append(book_data)

    # Сохранение данных в JSON-файл
    output_file = 'travel_books_data.json'
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(books_data, json_file, ensure_ascii=False, indent=2)

    print(f'Требуемая информация находится в файле {output_file}')

except Exception as e:
    print("Что-то пошло не так!")
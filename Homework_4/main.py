from lxml import html
import requests

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

url = 'https://www.ebay.com'
response = requests.get(url + '/b/Fishing-Equipment-Supplies/1492/bn_1851047', headers = header)

dom = html.fromstring(response.text)

names = dom.xpath("//h3[@class = 'textual-display.bsig__title__text']/text()")

print()
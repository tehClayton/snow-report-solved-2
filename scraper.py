from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.onthesnow.com/epic-pass/skireport.html'

html = requests.get(url).text
soup = bs(html, 'html.parser')

print(soup.prettify())
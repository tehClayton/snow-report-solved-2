from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

import requests

def init_browser():
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	return Browser('chrome', **executable_path, headless=False)


url = 'https://www.onthesnow.com/epic-pass/skireport.html'
browser = init_browser()
browser.visit(url)
time.sleep(3)
browser.execute_script("window.scrollTo(0, 5000);")
time.sleep(3)
browser.execute_script("window.scrollTo(0, 5000);")
time.sleep(3)

html = browser.html
browser.quit()

soup = bs(html, 'html.parser')
table = soup.find_all('table', class_='resortList')[0].find('tbody')


print(table.prettify())
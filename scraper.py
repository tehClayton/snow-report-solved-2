from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

import requests

def init_browser():
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	return Browser('chrome', **executable_path, headless=False)

def scrape_page():
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

	resort_rows = table.find_all('tr')
	resort_dict = {}
	for resort_row in resort_rows:
		# resort name
		resort_name = resort_row.find_all('td', class_='resort')[0].find('a').text
		# open status
		if 'background-color: rgb(28, 148, 0)' in resort_row.find_all('td', class_='openstate')[0].find('div')['style']:
			open_status = True
		else:
			open_status = False
		# new snow
		new_snow_list = resort_row.find_all('td', class_='nsnow')[0].find_all('b')
		new_snow_24_hr = new_snow_list[0].text.replace('"', '')
		new_snow_72_hr = new_snow_list[1].text.replace('"', '')
		# open lifts
		open_lifts_str = resort_row.find_all('td', class_='open_lifts')[0].text.replace(' ', '')
		open_lifts_str = f'0{open_lifts_str}' if open_lifts_str[0] == '/' else open_lifts_str
		open_lifts_list = open_lifts_str.split('/')
		open_lifts_pct = int(open_lifts_list[0])/int(open_lifts_list[1])
		# open trails
		open_trails_str = resort_row.find_all('td', class_='trails')[0].text.replace(' ', '')
		open_trails_str = f'0{open_trails_str}' if open_trails_str[0] == '/' else open_trails_str
		open_trails_list = open_trails_str.split('/')
		open_trails_pct = int(open_trails_list[0])/int(open_trails_list[1])
		resort_dict[resort_name] = {
		'open_status': open_status,
		'new_snow_24_hr': new_snow_24_hr,
		'new_snow_72_hr': new_snow_72_hr,
		'open_lifts_pct': open_lifts_pct,
		'open_trails_pct': open_trails_pct
		}

	return resort_dict


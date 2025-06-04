# this is a script for my friend jasper

# import libraries
from bs4 import BeautifulSoup
import csv
import requests_html
import time

# setup instructions:
# pip install requests_html
# pip install bs4

# these might not be necessary anymore
# pip install lxml_html_clean
# set pypeteer chromium revision to 1263111


# page url
potash_url = 'https://www.bathpotters.co.uk/potash-feldspar/p2284'

# csv filename
csv_name = 'potash.csv'

def generate_csv(url, file_name):
	with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
		writecsv = csv.writer(csvfile, delimiter=',')
		writecsv.writerow(["Name of Item", "Size option", "Price (GBP)", "Item Point Value", "Item URL"])

		print("Going to " + url)
		shop_session = requests_html.HTMLSession()
		shop_html = shop_session.get(url)

		
		# print(shop_html.html.text)

		shop_html.html.render()
		soup = BeautifulSoup(shop_html.html.raw_html, "lxml")
		# soup = BeautifulSoup(shop_html.html.text)
		# print(soup.prettify())

		items = soup.find_all(type="application/ld+json")[2]
		print(items.prettify())

		


generate_csv(potash_url,csv_name)

import requests
import csv, json
import time
from bs4 import BeautifulSoup
import pandas as pd 

df = pd.read_csv('petro_pages_main_category.csv')

profile = df['URL']

# profile = profile.iloc[::-1]

suppiler_csv = open('suppilers_petro_pages.csv', 'w')
csvwriter = csv.writer(suppiler_csv)

csvwriter.writerow(['supplier_Name','supplier_URL','supplier_category'])

for i in profile:
	page_url = i #'https://clutch.co/profile/apriorit#reviews'
	print "reveiwer detail--->", page_url
	page = requests.get(page_url)
	time.sleep(0.5)
	soup = BeautifulSoup(page.content, 'html.parser')
	row_provider = soup.find(class_="entrylist industrialCompressor").findAll('li')
	supplier_category = soup.find(class_="supComp").find('span').get_text()

	for i in row_provider:
		company_list = []
		Category_name = i.find('a').get_text()
		URL = i.a['href']
		print Category_name, URL

		company_list.append(Category_name.encode('ascii', 'ignore').decode('ascii'))
		company_list.append(URL.encode('ascii', 'ignore').decode('ascii'))
		company_list.append(supplier_category.encode('ascii', 'ignore').decode('ascii'))

		csvwriter.writerow(company_list)

suppiler_csv.close()
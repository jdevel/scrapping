import requests
import csv, json
import time
from bs4 import BeautifulSoup
import pandas as pd 

df = pd.read_csv('suppilers_petro_pages.csv')

profile = df['supplier_URL']
category = df['supplier_category']


suppiler_csv = open('all_suppilers_details2.csv', 'w')
csvwriter = csv.writer(suppiler_csv)

csvwriter.writerow(['supplier_Name','Contact_person','Address','Phone','Website','E-mail','supplier_Category'])

for index,i in enumerate(profile):
	page_url = i #'https://clutch.co/profile/apriorit#reviews'
	print "reveiwer detail--->", page_url
	page = requests.get(page_url)
	time.sleep(0.45)
	soup = BeautifulSoup(page.content, 'html.parser')
	#print soup.find(class_ = "teamIndustrialServices").find(class_ = "teamIndustrialServicesContactName").get_text().split(':')[1]

	try:
		supplier_name = soup.find(class_ = "teamIndustrialServices").find('h1').get_text()
	except:
		supplier_name = 'None'
	try:
		Contact_person = soup.find(class_ = "teamIndustrialServices").find(class_ = "teamIndustrialServicesContactName").get_text().split(':')[1]
	except:
		Contact_person = 'None'
	try:
		Address = soup.find(class_ = "teamIndustrialServices").find(class_ = "teamIndustrialServicesuUsername").get_text()
	except:
		Address = 'None'
	try:
		Phone = soup.find(class_ = "teamIndustrialServicesContact").find(class_ = "teamIndustrialServicesPhone").find('a').get_text()
	except:
		Phone = 'None'
	try:
		Website = soup.find(class_ = "teamIndustrialServicesContact").find(class_ = "teamIndustrialServicesWebsite").find('a').get_text()
	except:
		Website = 'None'
	try:
		Email = soup.find(class_ = "teamIndustrialServicesContact").find(class_ = "teamIndustrialServicesEmail").find('a').get_text()
	except:
		Email = 'None'

	supplier_category = category[index]


	company_list = []

	company_list.append(supplier_name.encode('ascii', 'ignore').decode('ascii'))
	company_list.append(Contact_person.encode('ascii', 'ignore').decode('ascii'))
	company_list.append(Address.encode('ascii', 'ignore').decode('ascii'))
	company_list.append(Phone.encode('ascii', 'ignore').decode('ascii'))
	company_list.append(Website.encode('ascii', 'ignore').decode('ascii'))
	company_list.append(Email.encode('ascii', 'ignore').decode('ascii'))
	company_list.append(supplier_category.encode('ascii', 'ignore').decode('ascii'))

	csvwriter.writerow(company_list)

	if (index%7 == 0):
		time.sleep(0.75)

suppiler_csv.close()
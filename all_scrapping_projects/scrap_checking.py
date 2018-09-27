import requests
import csv, json
import time, re
from bs4 import BeautifulSoup

page = requests.get("https://clutch.co/agencies")

soup = BeautifulSoup(page.content, 'html.parser')

# print soup.prettify()

row_provider = soup.find_all(class_="provider-row")

## row_provider = provider.find_all(class_="row provider-row-header")
## field_content = row_provider.find(class_="field-content")

## print row_provider[3].prettify()

company = row_provider[4].find(class_="field-content").get_text()
rating = row_provider[2].find(class_="rating").get_text() if row_provider[0].find(class_="rating") else 'None'
rate = row_provider[0].find(class_="hourly-rate").get_text() if row_provider[0].find(class_="hourly-rate") else 'None'
employee = row_provider[0].find(class_="employees").get_text() if row_provider[0].find(class_="employees") else 'None'
locality = row_provider[0].find(class_="locality").get_text() if row_provider[0].find(class_="locality") else 'None'
region = row_provider[0].find(class_="region").get_text() if row_provider[0].find(class_="region") else 'None'



min_project =row_provider[5].select(".module-list .list-item")[0].get_text()
website = row_provider[5].find(class_="website-link website-link-a").a['href']
mail_script = row_provider[5].find('div', attrs={'class' : 'contact-dropdown hide'}).find('script').get_text() #row_provider[4].select(".contact-dropdown  .item").a['href']
phone = row_provider[5].find('div', attrs={'class' : 'contact-dropdown hide'}).find('div', attrs={'class' : 'item __color6a'}).get_text() #row_provider[4].select(".contact-dropdown  .item").a['href']

profile = row_provider[5].find('div',attrs={'class':'col-xs-12 col-md-2 provider-link-details'}).find('ul',attrs={'class':'nav nav-pills nav-stacked nav-right-profile'}).find_all('li')[1].a['href']

full_profile = 'https://clutch.co'+profile

mail = row_provider[5].find('div', attrs={'class' : 'contact-dropdown hide'}).find('div', attrs={'class' : 'item'}).find('a')


print company, rating, min_project , website, phone, profile , "\n",full_profile ,  "\n", type(mail_script)

mail_script = str(mail_script)
mail_list = mail_script.split(' = ')
shuffle_name = mail_list[1].split(';')[0].replace("'","")
shuffle_pattern = mail_list[3].split(';')[0].split(']')

spera_name = shuffle_name.split('#')

final_name = ''
for pat in shuffle_pattern:
	if pat != '':
		print pat , "\n", pat[-1:] , type(pat[-1:]) , int(pat[-1:])
		final_name = final_name+spera_name[int(pat[-1:])]


print "\n", mail_list ,"\n", shuffle_name, "\n", shuffle_pattern ,"\n", spera_name,"\n", final_name

# m = [re.search(r"\[([A-Za-z0-9_]+)\]", shuffle_pattern)]
# print m
# soup = BeautifulSoup(thepage)
# for i in soup.find_all('div', attrs={'class' : 'project-card-content'}):
#     print(i.a['href'])

# scraping in walmart

import time
from selenium import webdriver
from time import sleep
import csv
import re , string 
# driver = webdriver.Firefox()
# time.sleep(5)
# driver.quit()
from lxml import html
# from pprint import pprint
# from xvfbwrapper import Xvfb 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select 

def init_driver():
	driver = webdriver.Firefox()
	# driver.wait = WebDriverWait(driver,35)
	return driver

def lookup(driver,query):
	driver.get("https://www.walmart.com/")
	try:
		searchKeyElement = driver.find_elements_by_xpath('//input[contains(@name,"query")]')
		submitButton  = driver.find_elements_by_xpath('//button[@type="submit"]')
		print type(submitButton)

		# box = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"global-search-input")))
		# # box = driver.wait.until(EC.presence_of_element_located((By.NAME,'query')))
		# button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME, "header-GlobalSearch-submit btn")))
		searchKeyElement[0].send_keys(query)
		submitButton[0].click()
		# content1 = driver.find_element_by_class_name('data_row').text
		# content = driver.find_element_by_tag_name('tbody').text
		parser = html.fromstring(driver.page_source, driver.current_url)

		print parser, driver.current_url
		sleep(3)

		Items = parser.xpath('//div[@id= "tile-container"]')
		# print Items
		Pro_lst, Pce_lst, Rev_lst = [],[],[]
		# print len(Items), "/n"

		for item in Items:
			# print "ITems"
			for it in item:
				# print "rounds"
				Pro = it.xpath('.//h4/a')
				Pce = it.xpath('.//span[@class = "price price-display"]')
				Rev = it.xpath('.//span[@class="js-reviews"]/span[@class = "visuallyhidden"]')

				if Pro:
					for pr in Pro:
						pr1 = str(pr.text_content())
						Pro_lst.append(pr1)
				else:
					Pro_lst.append('nill')


				if Pce:
					for pc in Pce:
						# print "Cycles"
						pc1 = str(pc.text_content())
						Pce_lst.append(pc1)
				else:
					Pce_lst.append('nill')

				if Rev:
					for re in Rev:
						# print "Cycles"
						re1 = str(re.text_content())
						Rev_lst.append(re1)
				else:
					Rev_lst.append('nill')



		# 	# for pro in ProductName0:
		# 	# 	print pro.text_content() , len(ProductName0)
		# 	# for pro in ProductName1:
		# 	# 	print pro.text_content(), len(ProductName1)		
		# 	# for pro in ProductName2:
		# 	# 	print pro.text_content(), len(ProductName2)


		# for item in Items:
		# 	print len(item)

		# 	if(i<len(item)):

		# 		ProductName = item[i].xpath('.//h4/a')
		# 		if ProductName:
		# 			ProductName.append(ProductName)
		# 		else:
		# 			ProductName.append("nill")

		# 		# print ProductName
		# 		# ProductName = ProductName[i].text_content() if ProductName else None
		# 		# Pro_lst.append(ProductName)			

		# 		Price = item[i].xpath('.//span[@class = "price price-display"]')
		# 		if Price:
		# 			Price.append(Price)
		# 		else:
		# 			Price.append('nill')
		# 		# print Price
		# 		# Price = Price[i].text_content() if Price else None
		# 		# Pce_lst.append(Price)

		# 		Reviews = item[i].xpath('.//span[@class="js-reviews"]/span[@class = "visuallyhidden"]')
		# 		if Reviews:
		# 			Reviews.append(Reviews)
		# 		else:
		# 			Reviews.append('nill')
		# 		# print Reviews
		# 		i +=1


		# 	# for pro in ProductName:
		# 	# 	Pro_lst.append(pro.text_content())

		# 	# for pre in Price:
		# 	# 	Pce_lst.append(pre.text_content()) 

		# 	# for revw in Reviews:
		# 	# 	Rev_lst.append(revw.text_content())


		# 	# total = {"ProductName":ProductName,"Price":Price}

		# 	# print(total)

		# print ProductName, Price, Reviews , len(ProductName), len(Price), len(Reviews)


		print Pro_lst,Pce_lst, Rev_lst , len(Pro_lst), len(Pce_lst), len(Rev_lst)

		# NextButton = driver.find_elements_by_xpath('//div[@id= "paginator-container"]/a[@class= "paginator-btn paginator-btn-next"]')

		for x in range(0,13):
			NextButton = driver.find_element_by_link_text('Next').click()
			sleep(3)
			# NextButton = driver.find_element_by_class_name('paginator-btn paginator-btn-next')
			print type(NextButton)
			# NextButton.click()
			sleep(5)
			Pro_lst,Pce_lst,Rev_lst = Rept_fun(driver,Pro_lst,Pce_lst,Rev_lst)



		print Pro_lst, Pce_lst, Rev_lst, len(Pro_lst), len(Pce_lst), len(Rev_lst)

		import pandas as pd

		df = pd.DataFrame()
		df['Product Name'] = Pro_lst
		df['Price'] = Pce_lst
		df['Reviews'] = Rev_lst
		# df['list'] = C

		print df

		df.to_csv('walmart_test.csv')

		# with open('walmr_check1.csv' , 'wb')as csvfile:
		# 	spamwriter = csv.writer(csvfile, delimiter =' ',quoting = csv.QUOTE_ALL)
		# 	spamwriter.writerow(Pro_lst)
		# 	spamwriter.writerow(Pce_lst)
		# 	spamwriter.writerow(Rev_lst)


	except TimeoutException:
		print ("Box or Content Not found in your given site")

def  Rept_fun(driver,Pro_lst,Pce_lst,Rev_lst):
	parser = html.fromstring(driver.page_source, driver.current_url)
	print parser, driver.current_url
	sleep(3)
	Items = parser.xpath('//div[@id= "tile-container"]')

	for item in Items:
		# print "ITems"
		for it in item:
			# print "rounds"
			Pro = it.xpath('.//h4/a')
			# Pce = it.find_element_by_class_name('price price-display')
			Pce = it.xpath('.//span[@class = "price price-display"]')  #//div[@class="tile-primary"]/div[@class="tile-row"]/div[@class="js-item-price-container item-price-container"]/
			Rev = it.xpath('.//span[@class="js-reviews"]/span[@class = "visuallyhidden"]')

			if Pro:
				for pr in Pro:
					pr1 = str(pr.text_content())
					# pr1 = str(pr1)
					Pro_lst.append(pr1)
			else:
				Pro_lst.append('nill')


			if Pce:
				for pc in Pce:
					# print "Cycles"
					# pc = pc.text_content()
					# pc.replace("\n","")
					pc1 = str(pc.text_content())
					pc1 =  pc1.replace('\n','')
					Pce_lst.append(pc1)

			else:
				Pce_lst.append('nill')

			if Rev:
				for re in Rev:
					# print "Cycles"
					re1 = str(re.text_content())
					Rev_lst.append(re1)
			else:
				Rev_lst.append('nill')

	return Pro_lst,Pce_lst,Rev_lst






if __name__ == "__main__":
	inp = input("Enter the product you need to search:")
	# inurl = str(inp)
	driver = init_driver()
	lookup(driver,inp)
	time.sleep(25)
	driver.quit()
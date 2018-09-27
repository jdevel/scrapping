# selenium web driver using unittest

import unittest
import codecs
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select 

from bs4 import BeautifulSoup

import urllib


oppge = "http://www.inc.com/inc5000/list/2016/"
page = urllib.urlopen(oppge)

soup = BeautifulSoup(page)

s1 = soup.title.string

print s1 
# list1 = soup.find('table' ,class_ = 'rank')

# A,B = [],[]

# for row in list1.find('dl'):
# 	cell = row.findAll('dt')
# 	col = row.findAll('dd')
# 	A.append(cell[0])
# 	B.append(cell[0])

# print A,B 

#print soup.prettify()

class PythonOgrSearch(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_search_in_python_or(self):
		driver = self.driver
		driver.get("http://www.inc.com/inc5000/list/2016/")						# navigation
		self.assertIn("The Full List",driver.title)
		# elem = driver.find_element_by_name("q")
		# cont = driver.find_element_by_id('column_headers').text
		content1 = driver.find_element_by_class_name('data_row').text
		content = driver.find_element_by_tag_name('tbody').text


		#select = Select(driver.find_element_by_class_name('responsive INC5000'))

	#	# con2 = driver.find_element_by_css_selector('div.column-next-to-badge-column').text

		#content2 = driver.find_elements(By.XPATH,'//dt').text
		#con1 = content.get_attribute('rank')
		# elem.send_keys("pycon",Keys.ARROW_UP)
		# #elem.send_keys(Keys.RETURN)
		#print con2
		# print select.select_by_class_name('rank').text
		# print con2

		# con2 = []
		B,C,D,E = [],[],[],[]

		# con2.append(content)	

		con_lst = content.splitlines()

		print  content , type(content) 

		# print con2 , len(con2) , type(con2)

		print con_lst , len(con_lst) , type(con_lst)

		for con in con_lst:
			C.append(str(con))

			# B.append(con.splitlines())

		# print B

		# C = [str(x) for x in B]
		print C

		import string 
		import re
		
		for ch in C:
			b_lst = re.findall(r'^[0-9]{1,2}',ch)
			B.append(b_lst)
			# print re.findall(r'+ +\d+,+%+\b',ch)     (?<=\ )[A-Za-z&0-9. ](?=\ )
			e_lst = re.findall(r'[A-Za-z&2. ]+ ',ch)   
			E.append(e_lst)

			d_lst = re.findall(r'[0-9,%]{6,7}',ch)[-1]
			D.append(d_lst)

		print B,E,D

		rank_lst = []
		for i in B:
			rank_lst +=i

		print rank_lst

		comp_lst = []
		for j in E:
			comp_lst +=j

		print comp_lst




		# chk_lst = [str(i) for i in con_lst.strip('[]').split(',')]
		# print chk_lst



		# print re.split('\W+', con_lst , flags=re.UNICODE)

		# print regex.split(con_lst)

		# for con in con_lst:
		# 	print con 
		# 	# B.append(con[0])
			# C.append(con[1])
			# D.append(con[2])

		# print B,C,D



		# print  content , type(content)
		# with codecs.open('sample22.txt','w',encoding = "utf-8") as d:
		# 	d.write(content)

		import pandas as pd

		df = pd.DataFrame()
		df['Rank'] = rank_lst
		df['Company'] = comp_lst
		df['Revenue Growth'] = D
		# df['list'] = C

		print df

		df.to_csv('my_chk_lst2.csv')


		with open('sel_chk4.csv' , 'wb')as csvfile:
			spamwriter = csv.writer(csvfile, delimiter =' ', quoting = csv.QUOTE_ALL)
			# spamwriter.writerow (['python']*5 + ['Ruby'])
			# spamwriter.writerow(['Python' ,'lovely lang.','wonderful lang'])
			spamwriter.writerow(con_lst)



		#print ("Value is : %s" %content.get_attribute("rank"))
		#print con1
		assert "No results Found." not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
import requests
import csv, json
import time, re
import pandas as pd 
import numpy as np

df = pd.read_csv('all_suppilers_with_state.csv')

#df['Address'].replace(np.NaN, 'None')
address = df['Address']
df['State'] = " "


for index,add in enumerate(address):
	print index
	if add != None:

		if re.search('(TX,|Tx,|Texas,|TEXAS,)', add):
			df['State'][index] = 'Texas'
		elif re.search('(NY,|Ny,|Newyork,)', add):
			df['State'][index] = 'Newyork'
		elif re.search('(NJ,|Nj,|New Jersy,)', add):
			df['State'][index] = 'New Jersy'	
		elif re.search('(CA,|Ca,|California,)', add):
			df['State'][index] = 'California'
		elif re.search('(FL,|Fl,|Florida,)', add):
			df['State'][index] = 'Florida'
		elif re.search('(KS,|Ks,|Kansas,)', add):
			df['State'][index] = 'Kansas'
		elif re.search('(VA,|Virginia,)', add):
			df['State'][index] = 'Virginia'
		elif re.search('(WI,|Wisconsin,)', add):
			df['State'][index] = 'Wisconsin'
		elif re.search('(GA,|Georgia,)', add):
			df['State'][index] = 'Georgia'
		elif re.search('(OK,|Oklahoma,)', add):
			df['State'][index] = 'Oklahoma'
		elif re.search('(LA,|Louisiana,)', add):
			df['State'][index] = 'Louisiana'
		elif re.search('(IN,|Indiana,)', add):
			df['State'][index] = 'Indiana'
		elif re.search('(IL,|Illinois,)', add):
			df['State'][index] = 'Illinois'
		elif re.search('(OH,|Ohio,)', add):
			df['State'][index] = 'Ohio'
		elif re.search('(OR,|Oregon,)', add):
			df['State'][index] = 'Oregon'
		elif re.search('(WA,|Washington,)', add):
			df['State'][index] = 'Washington'
		elif re.search('(KY,|Kentucky,)', add):
			df['State'][index] = 'Kentucky'
		elif re.search('(NV,|Nevada,)', add):
			df['State'][index] = 'Nevada'
		elif re.search('(MN,|Minnesota,)', add):
			df['State'][index] = 'Minnesota'
		elif re.search('(PA,|Pennsylvania,)', add):
			df['State'][index] = 'Pennsylvania'
		elif re.search('(MA,|Massachusetts,)', add):
			df['State'][index] = 'Massachusetts'
		elif re.search('(SD,|South Dakota,)', add):
			df['State'][index] = 'South Dakota'
		elif re.search('(MS,|Mississippi,)', add):
			df['State'][index] = 'Mississippi'
		elif re.search('(CO,|Colorado,)', add):
			df['State'][index] = 'Colorado'
		elif re.search('(WY,|Wyoming,)', add):
			df['State'][index] = 'Wyoming'
		elif re.search('(CANADA,|Canada,)', add):
			df['State'][index] = 'Canada'
		elif re.search('(SC,|South Carolina,)',	add):
			df['State'][index] = 'South Carolina'
		elif re.search('(NC,|North Carolina,)',	add):
			df['State'][index] = 'North Carolina'
		elif re.search('(CT,|Connecticut,)', add):
			df['State'][index] = 'Connecticut'
		elif re.search('(TN,|Tennessee,)', add):
			df['State'][index] = 'Tennessee'
		elif re.search('(AL,|Alabama,)', add):
			df['State'][index] = 'Alabama'
		elif re.search('(Canada,|Canada)', add):
			df['State'][index] = 'Canada'
		else:
			pass


df.to_csv('supplier_output.csv', index=False)
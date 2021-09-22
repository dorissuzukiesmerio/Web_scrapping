from bs4 import BeautifulSoup as BeautifulSoup

import pandas

# print("Hello")

import os

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

file_name = "html_files/coinmarketcap20210921161126.html"
f = open(file_name, "r")
# file_content = f.read()
# print(file_content)

soup = BeautifulSoup(f.read(), "html.parser")	
f.close()

# print(soup.find("tbody")) # prints everything from <tbody> to </tbody>
tbody = soup.find("tbody")
currency_rows = tbody.find_all("tr")

currency_row = currency_rows[0] # only reading the first one
currency_columns = currency_columns.find_all("td")
# Obs: the table structure is tr for rows, and td for the columns

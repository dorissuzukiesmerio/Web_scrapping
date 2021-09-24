from bs4 import BeautifulSoup as BeautifulSoup
import pandas

# print("Hello") # a good practice to check whether packages were installed and running; file on correct folder, etc

import os

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

file_name = "html_files/coinmarketcap20210921161126.html"
f = open(file_name, "r")
# file_content = f.read()
# print(file_content)
soup = BeautifulSoup(f.read(), "html.parser")	
f.close()

# print(soup.find("tbody")) # prints everything from <tbody> to </tbody>; correct; save it as an object:
tbody = soup.find("tbody")
currency_rows = tbody.find_all("tr") #within tbody, save all tr and save in object

for each_currency_row in currency_rows:
	# one_currency_row = currency_rows[0] # only reading the first one; before doing the loop
	currency_columns = each_currency_row.find_all("td")# Obs: the table structure is tr for rows, and td for the columns
	print(currency_columns[0].find("p").text) # the Name (Bitcoin)
	print(currency_columns[3].find("a").text) # the value 
	print(currency_columns[2].find("p", {"class": "coin-item-symbol"}))
	print(currency_columns[6].find(""))
	print() # getting the attribute of the tag. that is , the link
	 # getting the link of the picture: img, sc

# The choice:
 # we choose the one attribute that carries more meaning (and thus, is more stable)
# color is more dangerous, because it is more difficult to distinguish 


# First try for one cryptocurrency, then do the loop

# Error : when wrapping things inside the forloop; it meant that things worked for one row, but not for all.
# Use one more identifier to make sure the role you are using is actually using the role 
# When we decide to write the currency column, 
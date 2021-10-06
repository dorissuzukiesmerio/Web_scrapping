from bs4 import BeautifulSoup as BeautifulSoup
import pandas

# print("Hello") # a good practice to check whether packages were installed and running; file on correct folder, etc

import os
import glob

if not os.path.exists("deeplink_parsed_files"): # creating new folder to store the outputs; using this function to make directory with this name (the if statement is to make a folder with a unique name)
	os.mkdir("deeplink_parsed_files")

df = pandas.DataFrame()

# for file_name in glob.glob("deep_link_html/*.html"):
	file_name = "html_files/coinmarketcap20210921161126.html"
	scrape_time = os.path.basename(file_name).replace("coinmarketcap","").replace(".html","")
	f = open(file_name, "r") #r = reading; opening the connection to the file
	# file_content = f.read()
	# print(file_content)
	soup = BeautifulSoup(f.read(), "html.parser")	
	f.close() #good practice to avoid consuming more resources than necessary. Close after using it. (f is like the raw material of the soup. After cooking the soup , you don't need the raw material anymore, just the soup)

	# print(soup.find("tbody")) # prints everything from <tbody> to </tbody>; correct; save it as an object:
	tbody = soup.find("tbody")
	currency_rows = tbody.find_all("tr") #within tbody, save all tr and save in object

	for currency_row in currency_rows:
		# one_currency_row = currency_rows[0] # only reading the first one; before doing the loop
		currency_columns = currency_row.find_all("td")# Obs: the table structure is tr for rows, and td for the columns
		if len(currency_columns)>5:
			# print(scrape_time)
			currency_name = currency_columns[2].find("p").text # the Name (Bitcoin)
			currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","").replace(".","")# the value 
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"})
			currency_marketcap = currency_columns[6].find("p").find("span",{"class":"sc-1ow4cwt-1"}).text.replace("$","").replace(",","").replace(".","")
			currency_link = currency_columns[2].find("a")["href"] # getting the attribute of the tag. that is , the link to further info
			currency_image = currency_columns[2].find("img")["src"] # getting the link of the picture: img, sc

			df = df.append({ #from pandas
						'time':scrape_time,
						'name':currency_name,
						'price':currency_price,
						'symbol':currency_symbol,
						'marketcap':currency_marketcap,
						'link':currency_link,
						'image':currency_image
					}, ignore_index = True
			)

# {} 

# syntax :
# currency_columns[3] = the 4th td tag
# find("p")
# find("p", {"class": "something that uniquely identifies"})
# .text = get the text inside 
# ["href"] = get the attribute inside the specification; 
# links: are not the full links. They build up on the page's link - which we can add later

df.to_csv("parsed_files/coinmarketcap_dataset.csv")

import urllib.request
import os
import time # for oversleep time
import datetime

##### PART 1: DONWLOAD

if not os.path.exists("html_files"): # if this exists, don't make a new folder. if it doesn't, don't
	os.mkdir("html_files")

# # open webpage, read the content, and write into the content. 
# f = open("testing.html", "wb") #writing binary

# # Requesting the url 
# response = urllib.request.urlopen("http://coinmarketcap.com/") #sometimes it is useful to drop the s from https 
# html = response.read() #use the response and put into the read

# f.write(html) # writing that f into the variable html
# f.close()

#Download website every thirty minutes, for example. 

for i in range(5): # 1000 
	current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time) # good to see whether the forloop is actually running or not. So you can see the output
	#f = open("testing.html/testing"+str(i) + ".html", "wb") #writing binary
	f = open("html_files/coinmarketcap"+ current_time + ".html", "wb") #writing binary
	response = urllib.request.urlopen("http://coinmarketcap.com/") #sometimes it is useful to drop the s from https 
	html = response.read() #use the response and put into the read
	f.write(html) # writing that f into the variable html
	f.close()
	time.sleep(30) # 300 would be more appropriate in real world ( so the website doesn't block you)

# Comments:
# Change the name of the files so it doesn't overwrite
# So : timeseries of the cryptocurrency

#### PART 2: PARSING 
# Objective: transform to dataset in order to be able to make analysis



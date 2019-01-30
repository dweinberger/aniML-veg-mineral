# -*- coding: UTF-8 -*-
# -- DOWNLOADS PHOTOS FROM PIXABAY LISTED IN ALREADY-CREATED JSON FILES
import json 

import urllib.request

IMG_ROOT="images_fullsize/"

imageFileName="images/test.jpg"

#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') 


JSONFILE = "json/anivegamin-2.json"

json_data=open(JSONFILE).read()

data  = json.loads(json_data)
used = []
ctr = 0
dupectr = 0
for i in data:
	if i["webUrl"] in used:
		print("-- " + i["webUrl"] + " used")
		dupectr += 1
	else:
		used.append(i['webUrl'])
		filePath = IMG_ROOT + i["localFileName"]
		print(filePath)
		weburl = i['webUrl']
		#print(weburl)
		#weburl="https://pixabay.com/get/ea37b00d29fd033ed1584d05fb1d4594ea74e4d011ac104491f8c97fa2e4b2b9_640.jpg"
		urllib.request.urlretrieve(weburl, filePath)
		ctr += 1

print("--------DONE. LOOKED AT " + str(ctr) + " IMAGES. DUPES: " + str(dupectr) +  " USED:" + str(len(used)) + " ---------")
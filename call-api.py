# -*- coding: UTF-8 -*-
# -- GETS PHOTOS TAGGED IN ONE OF THREE CATEGORIES FROM PIXABAY
#    Animal, vege†able mineral
print("starting")
import json
from json import dumps, load
#print json.__file__         
import requests

fo=open("apikey", 'r')
apikey = fo.read()

APIKEY=apikey
pages_retrieved = 0
START_JSON_PAGE = 0
STARTING_PAGE="0"
LANG="en"
JSON_FILE="./json/allJson.json"
IMAGES_FOLDER = "./images_medium/"
NUMBER_OF_SPECIES_PER_KINGDOM = 15
NUMBER_OF_IMAGES_PER_SPECIES = 100
PER_PAGE=  "100"

 
print("FETCHING PHOTOS PIXABAY PHOTOS: ")
speciesList=[
"animal","dog","cat", "bird","person","shark","whale","bear","monkey","sparrow","fish", "insect","pig","bee", "face",
"vegetable","oak","rose","leaf","flower","corn","broccoli","tomato","pumpkin","tree","melon","apple","banana","grapes","seeds",
"mineral","rock","crystal","granite","stone","boulder","pebble","mountain","boulder","statue","marble","diamond","jewelry","cliff","pebbles"
] 

kingdoms=["animal","vegetable","mineral"]

totalSpeciesCtr = 0
kingdomNumber = 0
speciesNumber = 0
newjson = []



# -- Query for each species
for tag in speciesList:

	# -- query api for n images of a species
	
	queryurl = ("https://pixabay.com/api/?key=" + APIKEY + "&image_type=photo&per_page=" +
	PER_PAGE + "&starting_page=" + STARTING_PAGE + "&lang=en&safesearch=true&q=" + tag)
	print(queryurl)
	
	# do the call
	response = requests.get(queryurl)
	#print(response.content)
	#jsn=response.json()
	data  = response.json() #json.loads(response)
	
	# -- go through the n images of this species, adding them to the new json
	
	speciesctr = 0; # how many images of a species processed so far
	for i in data['hits']:
		localFileName = str(kingdomNumber) + "-" + str(speciesNumber) + "-"  +	str(i['id' ]) + 	".jpg"
		photo = {
			"tags" : i['tags'],
			"user_id" : i['user_id'],
			"userName" : i['user'],
			"previewURL" : i['previewURL'],
			"webUrl" : i['webformatURL'],
			"pageUrl" : i['pageURL'],
			"id"	: i['id'],
			"index" : totalSpeciesCtr,
			"kingdomNumber" : kingdomNumber,
			"kingdomName"	: kingdoms[kingdomNumber],
			"speciesNumber" : speciesNumber,
			"speciesName" : speciesList[speciesNumber],
			"userUrl" : i['userImageURL'],
			"localFileName" : localFileName
			}
		speciesctr += 1
		totalSpeciesCtr += 1
		# add the record to the json
		newjson.append(photo)
		
	# -- Gone through one species' images. Update counters	
	print("----" + str(speciesctr) + " images of " + speciesList[speciesNumber] + " kingdom:" + str(kingdomNumber) + " added to newjson")
	speciesNumber += 1
	# is this the last species in the kingdom?
	if (speciesNumber == 30):
		kingdomNumber = 2
	if (speciesNumber == 15):
		kingdomNumber = 1
with open("json/anivegamin-2.json", "w") as f:
     json.dump(newjson, f)

######---------- IGNORE
#d ata  = json.loads(json_data)
# ctr = 0;
# kingdomNumber = 0;
# speciesNumber = 0;
# speciesName = "monkey"
# kingdomName = "a"
# newjson = []
# for i in data['hits']:
# # 	tags=i['tags']
# # 	user_id=i['user_id']
# # 	weburl = i['webformatURL']
# 	photo = {
# 		"tags" : i['tags'],
# 		"user_id" : i['user_id'],
# 		"weburl" : i['webformatURL'],
# 		"pageurl" : i['pageURL'],
# 		"index" : ctr,
# 		"kingdomNumber" : kingdomNumber,
# 		"kingdomName"	: kingdomName,
# 		"speciesNumber" : speciesNumber,
# 		"speciesName" : speciesName,
# 		"userurl" : i['userImageURL']
# 	}
# 	ctr = ctr + 1
# 	newjson.append(photo)
# 	#print tags
# 		
# 		
# #print(newjson)
# 
# with open("newjson.json", "w") as f:
#     json.dump(newjson, f)
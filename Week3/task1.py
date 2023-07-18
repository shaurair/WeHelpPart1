# to disable verification for HTTPS connections to prevern urllib error on macOS
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as request
import json
import csv

# get data from internet
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
	data = json.load(response)

# analysis data and write to csv file
AttraList = data["result"]["results"]
MRTSet = {}

with open("attraction.csv", mode = "w", newline = "") as file:
	writer = csv.writer(file)

	for Attr in AttraList:
		writer.writerow([Attr["stitle"], Attr["address"].replace("臺北市  ","")[0:3], Attr["longitude"], Attr["latitude"], "https://"+Attr["file"].split("https://")[1]])

		# Check MRT info
		if Attr["MRT"] in MRTSet:
			MRTSet[Attr["MRT"]] += [Attr["stitle"]]
		elif Attr["MRT"] != None :
			MRTSet[Attr["MRT"]] = [Attr["MRT"],Attr["stitle"]]

with open("mrt.csv", mode = "w", newline = "") as file:
	writer = csv.writer(file)
	for mrt in MRTSet:
		writer.writerow(MRTSet[mrt])

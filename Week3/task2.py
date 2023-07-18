# to disable verification for HTTPS connections to prevern urllib error on macOS
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
import bs4
import csv

# get article post time
def GetArticleTime(url):
	request = req.Request(url, headers = {
		"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	})
	with req.urlopen(request) as response:
		data = response.read().decode("utf-8")
	root = bs4.BeautifulSoup(data, "html.parser")

	PostTime = root.find("span", string="時間").find_next("span", class_= "article-meta-value")
	if PostTime != None:
		return PostTime.string
	else:
		return ""

# get data from internet and write to file
def GetData(url, filewriter):
	request = req.Request(url, headers = {
		"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	})
	with req.urlopen(request) as response:
		data = response.read().decode("utf-8")
	root = bs4.BeautifulSoup(data, "html.parser")
	
	# get all article info list
	ListItem = root.find_all("div", class_= "r-ent")

	for i in range(len(ListItem)):
		RecNumber = ListItem[i].find_next("div", class_= 'nrec')

		if RecNumber.span != None:
			RecNumber = RecNumber.span.string
		else:
			RecNumber = 0

		Title = ListItem[i].find_next("div", class_='title')
		if Title.a != None:
			ArticleTime = GetArticleTime("https://www.ptt.cc/"+Title.a["href"])
			TitleName = Title.a.string
			filewriter.writerow([TitleName, RecNumber, ArticleTime])
	
	# return next page url
	nextLink = root.find("a", string = "‹ 上頁")
	return "https://www.ptt.cc/" + nextLink["href"]

# Get 3 Pages ptt Movie
PageURL = "https://www.ptt.cc/bbs/movie/index.html"
PageCnt = 0
with open("movie.txt", mode = "w", newline = "") as file:
	writer = csv.writer(file)
	while PageCnt < 3:
		PageURL = GetData(PageURL,writer)
		PageCnt += 1

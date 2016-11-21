#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
def getTitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj=BeautifulSoup(html.read(),'lxml')
		title=bsObj.body.h1
	except AttributerError as e:
		return None
	return title
	
title=getTitle("http://pythonscraping.com/pages/page1.html")
if title==None:
	print("title could not be found")
else:
	print(title)




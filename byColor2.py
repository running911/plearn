#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html.read(),"lxml")
#nameList=bsObj.findAll("span",{"class":"green"})
Just a test
#for name in nameList:
#	print(name.get_text())

print(bsObj)
hx=bsObj.findAll("h1")
print(hx)
 
#That is another copy

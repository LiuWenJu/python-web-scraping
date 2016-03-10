import urllib
import re


symbolsfile = open("symbols.txt")
symbolslist = symbolsfile.read()

#for symbol in symbolslist:
newsymbolslist =  symbolslist.split("\n")

#symbolslist = ["aapl","spy","goog","nflx"]

i = 0
while i < len(newsymbolslist):
    url = "http://finance.yahoo.com/q?s=" + newsymbolslist[i] + "&ql=1"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print "The price of " , newsymbolslist[i] ," is ",  price[0]
    i += 1



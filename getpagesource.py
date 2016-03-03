import urllib
import re

urls = ["https://www.google.com","https://www.bing.com","https://www.baidu.com","https://v2ex.com","https://www.youtube.com"]

i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)



while i < len(urls):

    htmlfile = urllib.urlopen(urls[i])

    htmltext = htmlfile.read()

    titles = re.findall(pattern,htmltext)

    print titles
    i += 1

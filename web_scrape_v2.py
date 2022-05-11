from bs4 import BeautifulSoup
import re
import urllib
import urllib3
from urllib.request import urlopen
import urllib.request
import sys


open('rawproxy.txt', 'w').close()
open('output.txt', 'w').close()

# read urls of websites from text file
list_url = open("test.txt")
read_list = list_url.read()
line_in_list = read_list.split("\n")

for url in line_in_list:
    page = urllib.request.urlopen(url, timeout=10, data=None)

    pageText = page.read()
    pageLines = page.readlines()
    stroutput = pageText.decode("utf-8")
    line_in_pageText = stroutput.split("\n")
    formatted_output = stroutput.replace('\\n', '\n').replace('\\t', '\t')
    # print(pageLines)
    # print(pageText)
    print(formatted_output)
    print(u''+formatted_output+'', file=open("rawproxy.txt", 'a', encoding='ascii'))


output = ""
with open("rawproxy.txt") as f:
    for line in f:
        if not line.isspace():
            output += line

f = open("output.txt", "w")
f.write(output)

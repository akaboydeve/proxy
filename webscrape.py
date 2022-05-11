from bs4 import BeautifulSoup
import re
import urllib
import urllib3
from urllib.request import urlopen


# read urls of websites from text file
list_open = open("weblist.txt")
read_list = list_open.read()
line_in_list = read_list.split("\n")

for url in line_in_list:
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html')
    # parse something special in the file
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        # extract information
        print(p.getText())

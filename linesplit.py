from bs4 import BeautifulSoup
import re
import urllib
import urllib3
from urllib.request import urlopen
import urllib.request
import sys


lines_per_file = 3800
smallfile = None
with open('output.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'proxy_{}.txt'.format(
                lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()

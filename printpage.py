import urllib.request

page = urllib.request.urlopen(
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt', data=None)


pageText = page.read()
pageLines = page.readlines()
stroutput = pageText.decode("utf-8")
line_in_pageText = stroutput.split("\n")
formatted_output = stroutput.replace('\\n', '\n').replace('\\t', '\t')
# print(pageLines)
# print(pageText)
print(formatted_output)
# print(line_in_pageText)

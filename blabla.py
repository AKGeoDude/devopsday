





from urllib import request
from bs4 import BeautifulSoup


url = 'http://www.bbc.co.uk'
h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

req = request.Request(url, headers=h)
with request.urlopen(req) as r:
	data = BeautifulSoup(r, 'html.parser')

title = data.title.string

with open(r'/data/scrapetitles', 'a') as f:
	f.write(title)


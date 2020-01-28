import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://www.youtube.com/')
bs = BS(r.content, 'html.parser')

title = []
href = []

for i in range(8):
	title_raw = bs.select('h3.yt-lockup-title > a')[i].text
	href_raw = bs.select('h3.yt-lockup-title > a')[i].get('href')
	title.append(title_raw)
	href.append(href_raw)

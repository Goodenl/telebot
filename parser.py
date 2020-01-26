import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://www.youtube.com/')
bs = BS(r.content, 'html.parser')

for i in range(8):
	title = bs.select('h3.yt-lockup-title > a')[i].text

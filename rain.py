from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.windguru.cz/263"
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
div = soup("div", {'id' : 'div_wgfcst0' })
tr = soup("tr", {'id' : 'tabid_0_0_APCPs' })

td_arr = str(tr).split('</td>')
idx = 0
for td in td_arr:
	idx = idx + 1
	if idx == 1:
		now = td[-1:]
		print('[{}]'.format(now))
	elif idx == 72:
		break
	elif idx < 70:
		print('[{}]'.format(td[-4:]))
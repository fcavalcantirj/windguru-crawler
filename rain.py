from bs4 import BeautifulSoup
from selenium import webdriver
import time

def fetch_html(url, sleep_in_sec):
	try:
		browser = webdriver.PhantomJS()
		browser.get(url)
		time.sleep(sleep_in_sec)
		html = browser.page_source
		return html
	except Exception as e:
		print(e);

def main():
	print('Starting windGuru crawler...')

	MAX_RETRIES = 5
	SLEEP_FOR = 5
	CURRENT = 1
	URL = "https://www.windguru.cz/263"

	while CURRENT <= MAX_RETRIES:

		print('trying nº {}'.format(CURRENT))
		
		html = fetch_html(URL, SLEEP_FOR)

		soup = BeautifulSoup(html, 'lxml')
		div = soup("div", {'id' : 'div_wgfcst0' })
		tr = soup("tr", {'id' : 'tabid_0_0_APCPs' })

		td_arr = str(tr).split('</td>')
		if not td_arr or len(td_arr) <= 1:
			print('DAAAAMMMMMNNN!!!')
			CURRENT += 1
			continue

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
		print('DONE')
		exit(0)


if __name__== "__main__":
	main()
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from itertools import chain
from datetime import datetime


def fetch_html(url, sleep_in_sec):
    try:
        browser = webdriver.PhantomJS()
        browser.get(url)
        time.sleep(sleep_in_sec)
        html = browser.page_source
        return html
    except Exception as e:
        print(e)


def fetch_html_headless(url, sleep_in_sec):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    driver = os.path.join(os.getcwd(), 'chromedriver')

    try:
        browser = webdriver.Chrome(chrome_options=options, executable_path=driver)
        browser.get(url)
        time.sleep(sleep_in_sec)
        html = browser.page_source
        return html
    except Exception as e:
        print(e)


def main():
    print('Starting windGuru crawler...')

    max_retries = 5
    sleep_for = 5
    current = 1
    url = "https://www.windguru.cz/263"

    for current in range(max_retries):
        print('trying nº {}'.format(current+1))

        html = fetch_html_headless(url, sleep_for)

        soup = BeautifulSoup(html, 'lxml')
        tr_dates = soup('tr', {'id': 'tabid_0_0_dates'})
        hours = [td.contents for td in chain.from_iterable([x.find_all('td') for x in tr_dates])]
        tr = soup("tr", {'id': 'tabid_0_0_APCPs'})
        td_arr = [td.contents[0] for td in chain.from_iterable([x.find_all('td') for x in tr])]
        if td_arr and hours:
            break
        else:
            print('DAAAAMMMMMNNN!!!')
            current += 1

    if not td_arr or not hours:
        print('Failed after {} tries')
        exit(0)

    dhoje = datetime.now().day
    forecast = filter(lambda x: int(x[0][2].strip('.')) == dhoje, zip(hours, td_arr))

    for h, p in forecast:
        print('{}: {}'.format(h[4], p))

    print('DONE')


if __name__ == "__main__":
    main()

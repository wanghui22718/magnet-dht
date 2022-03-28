import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def gdriver_demo():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:19222")


    path = '/usr/local/bin/chromedriver'
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
    # print(browser)
    url = 'https://h5-ocapp.onethingpcs.com/vPages/webapp/#/login'
    browser.get(url=url)
    for i in range(1, 11):
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight/10*%s);" % i
        )
        time.sleep(1)
    data = browser.page_source
    print(data)
    browser.quit()


def send_sms():
    url = 'https://user1.onethingpcs.com/xluser.core.login/v3/sendsms'



def whdht_deal_logs():
    with open('dhtlist.txt', 'r') as f:
        last_link = None
        total = {}
        for l in f.readlines():
            if l.startswith('magnet'):
                last_link = l
                continue
            if last_link:
                if last_link in total:
                    total[last_link] += int(l)
                else:
                    total[last_link] = int(l)
                last_link = None
        sorted_total = sorted(total.items(), key=lambda x:x[1], reverse=True)
        # return sorted_total
        count = 0
        for link in sorted_total:
            count += 1
            print(f'{link[0]} : {link[1]}')
        print(count)

if __name__ == "__main__":
    whdht_deal_logs()
    # gdriver_demo()
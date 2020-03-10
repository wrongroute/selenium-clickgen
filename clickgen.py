from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from concurrent.futures.thread import ThreadPoolExecutor
import asyncio

google = ('https://google.ru', 'q', 'LC20lb')
duck = ('https://duckduckgo.com', 'search_form_input_homepage', 'result')
bing = ('https://bing.ru', 'sb_form_q', 'b_title')
yandex = ('https://yandex.ru', 'text', 'organic__url-text')
mysite = 'site address'
mytitle = 'company title'

opts = Options()
opts.headless = True

def google_clicks(slink, formname, targetclass, title, site):
    for i in range(50):
        print('next iter google')
        browser = Firefox(options=opts)
        browser.get(slink)

        search_form = browser.find_element_by_name(formname)
        search_form.send_keys(site)
        search_form.submit()

        time.sleep(2)

        results = browser.find_elements_by_class_name(targetclass)
        time.sleep(2)

        for link in results:
            if link.text[0:7] == title:
                link.click()
                print('google click' + ' ' + browser.current_url)
                time.sleep(20)
                browser.quit()
                break
        time.sleep(10)


def duck_clicks(slink, formid, targetclass, title, site):
    for i in range(40):
        print('next iter duck')
        browser = Firefox(options=opts)
        browser.get(slink)

        search_form = browser.find_element_by_id(formid)
        search_form.send_keys(site)
        search_form.submit()

        time.sleep(2)

        results = browser.find_elements_by_class_name(targetclass)
        time.sleep(2)
        for link in results:
            if link.text[0:7] == title:
                link.click()
                print('duckduck click' + ' ' + browser.current_url)
                time.sleep(20)
                browser.quit()
                break
        time.sleep(10)


def bing_clicks(slink, formid, targetclass, title, site):
    for i in range(40):
        print('next iter bing')
        browser = Firefox(options=opts)
        browser.get(slink)

        search_form = browser.find_element_by_id(formid)
        search_form.send_keys(site)
        search_form.submit()

        time.sleep(2)

        results = browser.find_elements_by_class_name(targetclass)
        time.sleep(2)
        for link in results:
            if link.text[0:7] == title:
                link.click()
                print('bing click' + ' ' + browser.current_url)
                time.sleep(20)
                browser.quit()
                break
        time.sleep(10)



def yandex_clicks(slink, formid, targetclass, title, site):
    for i in range(40):
        print('next iter yandex')
        browser = Firefox(options=opts)
        browser.get(slink)

        search_form = browser.find_element_by_id(formid)
        search_form.send_keys(site)
        search_form.submit()

        time.sleep(2)

        results = browser.find_elements_by_class_name(targetclass)

        time.sleep(2)

        for link in results:
            if link.text[0:7] == title:
                link.click()
                print('yandex click' + ' ' + browser.current_url)
                time.sleep(20)
                browser.quit()
                break
        time.sleep(10)


loop = asyncio.get_event_loop()
pool = ThreadPoolExecutor(max_workers=5)

funclist = [loop.run_in_executor(pool, google_clicks, *google, mytitle, mysite),
            loop.run_in_executor(pool, yandex_clicks, *yandex, mytitle, mysite),
            loop.run_in_executor(pool, duck_clicks, *duck, mytitle, mysite)
            ]

loop.run_until_complete(
    asyncio.gather(*asyncio.all_tasks(loop))
)
loop.close()

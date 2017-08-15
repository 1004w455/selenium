# 참고사이트
# https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/

# driver
# Chrome    - https://sites.google.com/a/chromium.org/chromedriver/downloads
# PhantomJS - http://phantomjs.org/download.html


from selenium import webdriver

driver = webdriver.Chrome('/Users/1004w455/Documents/selenium/driver/chromedriver')
# driver = webdriver.PhantomJS('/Users/1004w455/Documents/selenium/driver/phantomjs')

driver.get('https://www.clien.net/service/group/allsell')

aTagArr = driver.find_elements_by_css_selector('#div_content div.card-grid div.item a.list-subject')

for a in aTagArr:
    print(a.text)

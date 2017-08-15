# 시작하기
## 1. 환경
- mac
- python(3)
- selenium
## 2. 설치
- python 설치 [다운](https://www.python.org/downloads/)
```
$ pip install selenium
```
## 3. webdriver
- [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) (/chromedriver 사용)
- [PhantomJS](http://phantomjs.org/download.html) (/bin/phantomjs 사용)
    - PhantomJS는 기본적으로 WebTesting을 위해 나온 Headless Browser다.(즉, 화면이 존재하지 않는다)
    - Binary 자체로 제공되기 때문에, Linux를 제외한 OS에서는 외부 dependency없이 바로 실행할 수 있다.
- 기타 여러 브라우저를 지원한다.
## 4. 사용하기
```python
from selenium import webdrver
driver = webdriver.Chrome('/드라이버위치/chromedriver')
driver.get('https://google.com')
...
```
import requests
from requests import session
from urllib.parse import quote
from bs4 import BeautifulSoup
from paddleocr import PaddleOCR
from datetime import datetime
class Browser:
    def __init__(self) -> None:
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        self.session = session()
        self.msg = ''
        self.ocr = PaddleOCR()

    def login(self):
        url = 'https://cas.bnu.edu.cn/cas/login'
        response = self.session.get(url)
        if response.status_code != 200:
            raise ConnectionError('登录状态码非200')
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text,'lxml')
        lt = soup.select_one('#lt')['value']

        # un = '202121250011'
        # pd = 'xysz402715'
        JSESSIONID = self.session.cookies.get('JSESSIONID','')
        param = {
            'rsa' : PyJsHoisted_strEnc_(un+pd+lt,'1','2','3'),
            'ul' : str(len(un)),
            'pl' : str(len(pd)),
            'lt' : lt,
            'execution' : soup.select_one('input[name=execution]')['value'],
            '_eventId' : soup.select_one('input[name=_eventId]')['value'],
        }
        res = self.session.post(
            url='http://cas.bnu.edu.cn/cas/login;jsessionid='+JSESSIONID+'?service=https%3A%2F%2Fcgyd.prsc.bnu.edu.cn%2Flogin.jsp',
            data=param,headers=self.header,
        )

        self.session.post()


if __name__=='__main__':
    browser = Browser()
    browser.login()
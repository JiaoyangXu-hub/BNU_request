# import urllib.request
# import time,random,os
# from urllib.request import Request
# from urllib import request
# import requests
# request

import re
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
# pubkey,privkey = rsa.newkeys(1024)
# crypto = rsa.encrypt(message, pubkey)
# message = rsa.decrypt(crypto, privkey)

# param_dict={}
# param = urlencode(param_dict)
# url = 'http://cas.bnu.edu.cn/cas/login'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }

url = 'http://cas.bnu.edu.cn/cas/login?service=https%3A%2F%2Fcgyd.prsc.bnu.edu.cn%2Flogin.jsp'
session = requests.session()
response = session.get(url=url,headers=header)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,'lxml')

lt=soup.select_one('#lt')['value']
execution = soup.select_one('input[name=execution]')['value']
_eventId = soup.select_one('input[name=_eventId]')['value']
un = '202121250011'
pd = 'xysz402715'
ul = str(len(un))
pl = str(len(pd))

# context = js2py.EvalJs()
# from JS import JS
from des import PyJsHoisted_strEnc_
# context.execute(JS)
rsa = PyJsHoisted_strEnc_(un+pd+lt,'1','2','3')
# rsa=context.strEnc(un+pd+lt,'1','2','3')
JSESSIONID = session.cookies.get('JSESSIONID','')
param = {
	'rsa': rsa,
	'ul': ul,
	'pl': pl,
	'lt': lt,
	'execution': execution,
	'_eventId': _eventId,
}
res=session.post(
	url='http://cas.bnu.edu.cn/cas/login;jsessionid='+JSESSIONID+'?service=https%3A%2F%2Fcgyd.prsc.bnu.edu.cn%2Flogin.jsp',
	data=param,headers=header
	)

r = session.post(
	url='https://cgyd.prsc.bnu.edu.cn/gymbook/gymBookAction.do?ms=hadContactOrNot',
	data={'ms': 'hadContactOrNot'},
	headers=header
)

jpg = session.get(url='https://cgyd.prsc.bnu.edu.cn/Kaptcha.jpg',stream=True)
if jpg.status_code == 200:
	with open('checkcode.jpg','wb') as j:
		j.write(jpg.content)
from paddleocr import PaddleOCR
from re import findall

ocr = PaddleOCR()
def cal_val_code(img:str):
    '''
    采用paddleOCR识别和计算验证码的值
    若输入是字符串地址
    '''
    ocr_res = ocr.ocr(img,cls=False)[0][1]
    expre = findall(r'[0-9]{1,2}? *?[+-] *?[0-9]{1,2}',ocr_res[0])
    # 若识别匹配率到0.8以上且匹配到的pattern只有一个
    if ocr_res[1]>0.8 and len(expre)==1:
        return int(eval(expre[0]))  # 返回结果
    else:
        return float(ocr_res[1])    # 返回匹配识别率
check_res = cal_val_code('./checkcode.jpg')
param = {
	'bookData.totalCost': '',
	'bookData.book_person_zjh': '',
	'bookData.book_person_name': '',
	'bookData.book_person_phone': '16601296123',
	'gymnasium_idForCache': '2',
	'item_idForCache': '5462',
	'time_dateForCache': '2022-08-27',
	'userTypeNumForCache': '1',
	'putongRes': 'putongRes',
	'selectedPayWay': '1',
	'allFieldTime': '69208#2022-08-27',
	'companion_1': '',
	'companion_2': '',
	'companion_3': '',
	'companion_4': '',
	'companion_5': '',
	'companion_6': '',
	'companion_7': '',
	'companion_8': '',
	'companion_9': '',
	'checkcodeuser': check_res,
	'selectPayWay': '1',
}
resp = session.post(
	url='https://cgyd.prsc.bnu.edu.cn/gymbook/gymbook/gymBookAction.do?ms=saveGymBook',
	data=param,headers=header,
)
if re.search('预定成功',resp.text):
	pass


response.text

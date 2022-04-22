# -*- coding: utf-8 -*-
from io import BytesIO
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from paddleocr import PaddleOCR
import time,datetime,re,os,requests
from PIL import Image


id = '202121250011'
# pwd = input('输入id对应的密码：')
pwd = 'xysz402715'
tel = '16601296123'
name = '徐骄阳'
selec = '羽毛球'
num_fetch = 1 #预定几个格子
# tmp_img = 'tmp_img.png'
ocr = PaddleOCR()

# option = webdriver.ChromeOptions()
# option.add_argument('headless')  # 设置option
# driver = webdriver.Chrome(options=option)  # 调用带参数的谷歌浏览器
driver = webdriver.Chrome()
driver.get('http://cas.bnu.edu.cn/cas/login?service=https%3A%2F%2Fcgyd.prsc.bnu.edu.cn%2Flogin.jsp')

def cal_val_code(img:str):
    '''
    采用paddleOCR识别和计算验证码的值
    若输入是字符串地址
    '''
    ocr_res = ocr.ocr(img,cls=False)[0][1]
    expre = re.findall(r'[0-9]{1,2}? *?[+-] *?[0-9]{1,2}',ocr_res[0])
    # 若识别匹配率到0.8以上且匹配到的pattern只有一个
    if ocr_res[1]>0.8 and len(expre)==1:
        return int(eval(expre[0]))  # 返回结果
    else:
        return float(ocr_res[1])    # 返回匹配识别率


def cal_val_code(img:Image.Image):
    '''
    采用paddleOCR识别和计算验证码的值
    若输入是Image
    '''
    img.convert('L')
    ocr = PaddleOCR()
    ocr_res = ocr.ocr(np.asarray(img),cls=False)[0][1]
    expre = re.findall(r'[0-9]{1,2}? *?[+-] *?[0-9]{1,2}',ocr_res[0])
    if ocr_res[1]>0.8 and len(expre)==1:
        return int(eval(expre[0]))  # 返回结果
    else:
        return float(ocr_res[1])    # 返回匹配识别率


def wait_until(hour:int=7,minute:int=29,second:int=0,check_freq=60):
    '''
    定时唤醒
    '''
    while True:
        now = datetime.datetime.now()
        print(now)
        if now.hour >= hour and now.minute >= minute and now.second >= second:
            break
        else:
            time.sleep(check_freq)
    return None





def wait_element(selector:str) -> WebElement:
    return WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,selector)))[0]

def click_blank_cell(tb:WebElement,num:int=1)->bool:
    '''
    选择前num个没被预定的格子
    '''
    # TODO：做一个时间的筛选，免得整到八点了
    # for span in tb.find_elements_by_css_selector('.resourceTr'):
    #     if span in 
    for unit in tb.find_elements_by_css_selector('td'):
        if not unit.get_attribute('bookid'):
            # 点击空闲格子
            unit.click()
            num -= 1
        if num==0:
            return True
    return False

if __name__=='__main__':


    # 休眠
    # wait_until(hour=7,minute=29,second=0)

    # 等待元素加载
    wait_element('#un').clear()
    wait_element('#pd').clear()

    # 登录
    driver.find_element_by_css_selector('#un').send_keys(id)
    driver.find_element_by_css_selector('#pd').send_keys(pwd)
    wait_element('#index_login_btn').click()

    '''
    跳转到体育馆预约页面
    '''

    driver.implicitly_wait(30)
    # 关弹窗
    # time.sleep(0.2)
    driver.find_element_by_css_selector('[onclick="saveAttentionState()"]').click()

    item = {'乒乓球':'1','网球':'2','羽毛球':'3'}

    # 开始抢
    while True:

        # 选羽毛球
        order = driver.find_elements_by_css_selector('#tabs > ul > li:nth-child({}) > a'.format(item[selec]))

        if len(order)==1:   #如果有指定球类选项卡
            order[0].click()
            break
        else:               #否则刷新，等待网页加载，停0.2s
            driver.refresh()
            driver.implicitly_wait(30)
            time.sleep(0.2)

    #选择球类后

    # 等待日期选项卡加载
    wait_element('.datetime_')

    # 选择最后一个日期选项
    lst = driver.find_elements_by_css_selector('.datetime_')
    lst[-1].click()

    # 定位时间表格
    driver.switch_to.frame('overlayView')
    tb = driver.find_element_by_css_selector('#resourceTable')

    tf = click_blank_cell(tb,num_fetch)
    if tf:
        # 点击预定
        driver.switch_to.default_content()
        driver.find_element_by_css_selector('[onclick="saveOdder()"]').click()
        # 捕获验证码的位置
        val_code_img = wait_element('#kaptchaImage')
        while True:
            loc = val_code_img.location
            s = val_code_img.size
            if loc['x']*loc['y']*s['width']*s['height']:
                break
        # driver.execute_script('document.body.style.zoom=1')#缩放比例
        img_data = driver.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(img_data))
        # screenshot.crop((
        #     loc['x'],loc['y'],
        #     loc['x']+s['width'],loc['y']+s['height']
        # )).save(tmp_img)

        val_code = screenshot.crop((
            530,380,
            530+s['width']+20,380+s['height']+20
        )).convert('L')#裁剪转灰度图

        ## request不太合适
        # driver.find_element_by_css_selector('#kaptchaImage').get_attribute('src')
        # cookies = driver.get_cookies()
        # cookies = {cookie['name']:cookie['value'] for cookie in cookies}
        # response = requests.get(url='https://cgyd.prsc.bnu.edu.cn/Kaptcha.jpg',headers='',cookies=cookies)
        # if response.status_code==200:
        #     # if not os.path.exists('tmp_img/'):
        #     #     os.mkdir('tmp_img/')
        #     with open('val_code.jpg','wb') as f:
        #         f.write(response.content)
        
        # OCR识别验证码
        res = cal_val_code(val_code)
        # 输入验证码
        driver.find_element_by_css_selector('#checkcodeuser').send_keys(str(res))
        # 输入姓名
        driver.find_element_by_css_selector('#companion_1').send_keys(name)
        # 点击提交
        driver.find_element_by_css_selector('[onclick="saveBookFrmWithPay()"]').click()
        # 稍后支付
        driver.find_element_by_css_selector('[onclick="payLater()"]').click()
    else:
        print("位置抢完了，明天再来")
# # 若弹窗

# if driver.find_elements_by_css_selector('#contactModal'):
#     driver.find_element_by_css_selector('#cell_phone').send_keys(tel)
#     driver.find_element_by_css_selector('#telform > input[type=button]:nth-child(3)').click()
#     alert = driver.switch_to.alert
#     alert.accept()
#     driver.find_element_by_css_selector('#box-0 > div > div > div.pull-right > span > a > span > span > i').click()

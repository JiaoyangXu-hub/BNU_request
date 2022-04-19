from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
# import pandas as pd

id = '202121250011'
pwd = 'xysz402715'
tel = '16601296123'
selec = '羽毛球'


driver = webdriver.Chrome()

driver.get('http://cas.bnu.edu.cn/cas/login?service=https%3A%2F%2Fcgyd.prsc.bnu.edu.cn%2Flogin.jsp')

# wait_element = lambda selector : WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located(By.CSS_SELECTOR,selector))
def wait_element(selector:str) -> WebElement:
    return WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,selector)))[0]
# 等待元素加载

wait_element('#un').clear()
wait_element('#pd').clear()
# 登录
driver.find_element_by_css_selector('#un').send_keys(id)
driver.find_element_by_css_selector('#pd').send_keys(pwd)
wait_element('#index_login_btn').click()

# 抢
# 关弹窗
driver.implicitly_wait(30)
driver.find_element_by_css_selector('#attentionModal > div.modal-footer > button').click()

# 选羽毛球
item = {'乒乓球':'1','网球':'2','羽毛球':'3'}
driver.find_element_by_css_selector('#tabs > ul > li:nth-child({}) > a'.format(item[selec])).click()

# 选择日期最后一个
lst = driver.find_elements_by_css_selector('#box-0 > div > div > div.pull-left > a')
lst[-1].click()
# 预约时间
driver.switch_to.frame('overlayView')
tb = driver.find_element_by_css_selector('#resourceTable')

# data = pd.read_html(driver.page_source)
# 选择第一个没被预定的格子
for unit in tb.find_elements_by_css_selector('td'):
    if not unit.get_attribute('bookid'):
        unit.click()
        driver.switch_to.default_content()

        # 预约
        driver.find_element_by_css_selector('#box-0 > div > div > div.pull-right > span > a > span > span > i').click()

        break
    print('场地已被抢空，下次再来')
# 若弹窗

if driver.find_elements_by_css_selector('#contactModal'):
    driver.find_element_by_css_selector('#cell_phone').send_keys(tel)
    driver.find_element_by_css_selector('#telform > input[type=button]:nth-child(3)').click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element_by_css_selector('#box-0 > div > div > div.pull-right > span > a > span > span > i').click()

# 点击预约


a = 1

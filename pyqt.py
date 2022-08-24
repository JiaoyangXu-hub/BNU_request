# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gymNOagGh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from io import BytesIO
from sys import argv,exit
from re import match
from PySide2.QtCore import QDateTime,QDate,QTime,QMetaObject,QCoreApplication
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QGridLayout,QLabel,QTextBrowser,QDateTimeEdit,QComboBox,QLineEdit,QSpinBox,QSlider,QLCDNumber,QDialogButtonBox,QFrame,QWidget,QApplication
from datetime import datetime
from time import sleep,time
from main import cal_val_code,click_blank_cell,wait_element,wait_until
from selenium.webdriver import Chrome
from paddleocr import PaddleOCR
from selenium.webdriver.common.by import By

_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Ui_BNU_GYM(object):
    def __init__(self) -> None:
        ui = QWidget()
        self.setupUi(ui)
        ui.show()


        # 设置为0.6秒一次访问
        self.Rate.setValue(6)
        # 设置时间为当前时间
        self.From.setDateTime(QDateTime().fromString(_datetime,format='%Y-%m-%d %H:%M:%S'))
        self.To.setDateTime(QDateTime().fromString(_datetime,format='%Y-%m-%d %H:%M:%S'))
        # 点击两个按钮
        self.buttonBox.accepted.connect(self.click_ok)
        self.buttonBox.rejected.connect(self.click_cancel)
        exit(app.exec_())
    def freeze(self,tf:bool=True):
        '''冻结所有box，除了cancel和文本框'''
        self.Id.setDisabled(tf)
        self.Name.setDisabled(tf)
        self.Pwd.setDisabled(tf)
        self.Tel.setDisabled(tf)
        self.From.setDisabled(tf)
        self.To.setDisabled(tf)
        self.Rate.setDisabled(tf)
        self.buttonBox.AcceptRole.setDisabled(tf)

    def click_ok(self):
        self.buttonBox.AcceptRole.setEnabled(False)
        self.textBrowser.setText('Start ! ! \n')
        self.textBrowser.append('check info ... \n')
        id = self.Id.text().strip()
        name = self.Name.text().strip()
        pwd = self.Pwd.text().strip()
        tel = self.Tel.text().strip()
        _from = self.From.dateTime().toTime_t()
        _to = self.To.dateTime().toTime_t()
        rate = self.Rate.value()/10
        rate = max(min(rate,5),min(0.1,rate))

        self.freeze(True)

        if not match(r'^20[12][0-9]{9}$',id):
            self.textBrowser.append(' - {} get wrong..\n----------------\n'.format('id'))
            self.Id.selectAll()
            self.textBrowser.append(' processing stopped \n')
            self.freeze(False)
        elif not name:
            self.textBrowser.append(' - {} get wrong..\n----------------\n'.format('name'))
            self.Name.selectAll()
            self.textBrowser.append(' processing stopped \n')
            self.freeze(False)
        elif not pwd:
            self.textBrowser.append(' - {} get wrong..\n----------------\n'.format('pwd'))
            self.Pwd.selectAll()
            self.textBrowser.append(' processing stopped \n')
            self.freeze(False)
        elif not match(r"^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$",tel):
            self.textBrowser.append(' - {} get wrong..\n----------------\n'.format('tel'))
            self.Tel.selectAll()
            self.textBrowser.append(' processing stopped \n')
            self.freeze(False)
        elif _from >= _to:
            self.textBrowser.append(' - {} get wrong..\n----------------\n'.format('time range'))
            self.textBrowser.append(' processing stopped \n')
            self.freeze(False)
        else:
            self.id = id
            self.name = name
            self.pwd = pwd
            self.tel = tel
            self._from = _from
            self._to = _to
            self.rate = rate
            self.textBrowser.append('finish check ~ \n----------------\n - process will begin at {}:{}:{}\n'.format('07','29','00'))
            self.wait_until(hour=7,minute=29,second=0)
            self.textBrowser.append('\n === processing begin === \n')
            self.time_begin = time()
            self.main_process()


    def main_precess(self):
        """
        主要流程
        """
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')  # 设置option
        # driver = webdriver.Chrome(options=option)  # 调用带参数的谷歌浏览器
        driver = Chrome()
        driver.get('http://cas.bnu.edu.cn/cas/login?service=https%3A%2F%2Fcgyd.prsc.bnu.edu.cn%2Flogin.jsp')

        ocr = PaddleOCR()
        # 休眠
        # wait_until(hour=7,minute=29,second=0)

        # 等待元素加载
        wait_element('#un').clear()
        wait_element('#pd').clear()

        # 登录
        driver.find_element_by_css_selector('#un').send_keys(self.id)
        driver.find_element_by_css_selector('#pd').send_keys(self.pwd)
        wait_element('#index_login_btn').click()

        '''
        跳转到体育馆预约页面
        '''

        driver.implicitly_wait(30)
        # 关弹窗
        # time.sleep(0.2)
        driver.find_element_by_css_selector('[onclick="saveAttentionState()"]').click()

        item = {'乒乓球':'1','网球':'2','羽毛球':'3'}
        self.type = self.comboBox.currentText().strip()

        # 开始抢
        while True:

            order = driver.find_elements_by_css_selector('#tabs > ul > li:nth-child({}) > a'.format(item[self.type]))

            if len(order)==1:   #如果有指定球类选项卡
                order[0].click()
                break
            else:               #否则刷新，等待网页加载，停0.2s
                driver.refresh()
                driver.implicitly_wait(30)
                sleep(0.2)

        #选择球类后

        # 等待日期选项卡加载
        wait_element('.datetime_')

        # 选择最后一个日期选项
        lst = driver.find_elements_by_css_selector('.datetime_')
        lst[-1].click()

        # 定位时间表格
        driver.switch_to.frame('overlayView')
        tb = driver.find_element_by_css_selector('#resourceTable')

        tf = click_blank_cell(tb,self.Num.value())
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
            screenshot = open(BytesIO(img_data))
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
            driver.find_element(by=By.CSS_SELECTOR,value='#checkcodeuser').send_keys(str(res))
            
            # 输入姓名
            driver.find_element(by=By.CSS_SELECTOR,value='#companion_1').send_keys(self.name)
            # 点击提交
            driver.find_element(by=By.CSS_SELECTOR,value='[onclick="saveBookFrmWithPay()"]').click()
            # 稍后支付
            driver.find_element(by=By.CSS_SELECTOR,value='[onclick="payLater()"]').click()
        else:
            # print("位置抢完了，明天再来")
            self.textBrowser.append("There's no blank, please check tomorrow ~ \n")
    # # 若弹窗

    # if driver.find_elements_by_css_selector('#contactModal'):
    #     driver.find_element_by_css_selector('#cell_phone').send_keys(tel)
    #     driver.find_element_by_css_selector('#telform > input[type=button]:nth-child(3)').click()
    #     alert = driver.switch_to.alert
    #     alert.accept()
    #     driver.find_element_by_css_selector('#box-0 > div > div > div.pull-right > span > a > span > span > i').click()


    def click_cancel(self):
        '''需要一个线程关闭主线程'''
        pass

    def setupUi(self, BNU_GYM):
        if not BNU_GYM.objectName():
            BNU_GYM.setObjectName(u"BNU_GYM")
        BNU_GYM.resize(816, 642)
        self.gridLayout = QGridLayout(BNU_GYM)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(BNU_GYM)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)

        self.comboBox = QComboBox(BNU_GYM)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(BNU_GYM)
        # self.buttonBox.button(QDialogButtonBox.Ok).setDefault(True) #TODO
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 4, 1, 1)

        self.line_2 = QFrame(BNU_GYM)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 5, 5, 1)

        self.label = QLabel(BNU_GYM)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.To = QDateTimeEdit(BNU_GYM)
        self.To.setObjectName(u"To")
        self.To.setDateTime(QDateTime(QDate(2022, 8, 23), QTime(0, 0, 0)))
        self.To.setCalendarPopup(True)

        self.gridLayout.addWidget(self.To, 2, 4, 1, 1)

        self.Id = QLineEdit(BNU_GYM)
        self.Id.setObjectName(u"Id")
        self.Id.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.gridLayout.addWidget(self.Id, 0, 1, 1, 1)

        self.Runtime = QLCDNumber(BNU_GYM)
        self.Runtime.setObjectName(u"Runtime")
        self.Runtime.setDigitCount(5)
        self.Runtime.setSegmentStyle(QLCDNumber.Flat)
        self.Runtime.setProperty("value", 0.000000000000000)
        self.Runtime.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.Runtime, 3, 4, 1, 1)

        self.label_6 = QLabel(BNU_GYM)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)

        self.line = QFrame(BNU_GYM)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 5, 1)

        self.label_7 = QLabel(BNU_GYM)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.Num = QSpinBox(BNU_GYM)
        self.Num.setObjectName(u"Num")
        self.Num.setMaximum(5)
        self.Num.setValue(1)

        self.gridLayout.addWidget(self.Num, 3, 1, 1, 1)

        self.Tel = QLineEdit(BNU_GYM)
        self.Tel.setObjectName(u"Tel")
        self.Tel.setInputMethodHints(Qt.ImhDialableCharactersOnly)

        self.gridLayout.addWidget(self.Tel, 1, 4, 1, 1)

        self.Pwd = QLineEdit(BNU_GYM)
        self.Pwd.setObjectName(u"Pwd")
        self.Pwd.setInputMethodHints(Qt.ImhHiddenText)

        self.gridLayout.addWidget(self.Pwd, 1, 1, 1, 1)

        self.label_5 = QLabel(BNU_GYM)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.From = QDateTimeEdit(BNU_GYM)
        self.From.setObjectName(u"From")
        self.From.setDateTime(QDateTime(QDate(2022, 8, 23), QTime(0, 0, 0)))
        self.From.setCalendarPopup(True)

        self.gridLayout.addWidget(self.From, 2, 1, 1, 1)

        self.textBrowser = QTextBrowser(BNU_GYM)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setContextMenuPolicy(Qt.NoContextMenu)

        self.gridLayout.addWidget(self.textBrowser, 0, 6, 5, 1)

        self.Rate = QSlider(BNU_GYM)
        self.Rate.setObjectName(u"Rate")
        self.Rate.setMinimum(1)
        self.Rate.setValue(50)
        self.Rate.setOrientation(Qt.Horizontal)
        self.Rate.setInvertedAppearance(False)
        self.Rate.setTickPosition(QSlider.TicksAbove)
        self.Rate.setTickInterval(10)

        self.gridLayout.addWidget(self.Rate, 4, 4, 1, 1)

        self.label_9 = QLabel(BNU_GYM)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_4 = QLabel(BNU_GYM)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.label_3 = QLabel(BNU_GYM)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(BNU_GYM)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_10 = QLabel(BNU_GYM)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)

        self.Name = QLineEdit(BNU_GYM)
        self.Name.setObjectName(u"Name")

        self.gridLayout.addWidget(self.Name, 0, 4, 1, 1)

        self.label_11 = QLabel(BNU_GYM)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 6, 1, 1)

        QWidget.setTabOrder(self.Id, self.Name)
        QWidget.setTabOrder(self.Name, self.Pwd)
        QWidget.setTabOrder(self.Pwd, self.Tel)
        QWidget.setTabOrder(self.Tel, self.From)
        QWidget.setTabOrder(self.From, self.To)
        QWidget.setTabOrder(self.To, self.Num)
        QWidget.setTabOrder(self.Num, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.Rate)
        QWidget.setTabOrder(self.Rate, self.textBrowser)

        self.retranslateUi(BNU_GYM)
        self.buttonBox.accepted.connect(self.textBrowser.clear)
        self.From.dateTimeChanged.connect(self.To.setDateTime)
        self.comboBox.currentIndexChanged.connect(self.Num.clear)

        QMetaObject.connectSlotsByName(BNU_GYM)
    # setupUi

    def retranslateUi(self, BNU_GYM):
        BNU_GYM.setWindowTitle(QCoreApplication.translate("BNU_GYM", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("BNU_GYM", u"Runtime", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("BNU_GYM", u"\u7fbd\u6bdb\u7403", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("BNU_GYM", u"\u4e52\u4e53\u7403", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("BNU_GYM", u"\u7f51\u7403", None))

        self.label.setText(QCoreApplication.translate("BNU_GYM", u"Id", None))
        self.Id.setText("")
        self.Id.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("BNU_GYM", u"To", None))
        self.label_7.setText(QCoreApplication.translate("BNU_GYM", u"Num", None))
        self.Tel.setText("")
        self.Pwd.setText("")
        self.label_5.setText(QCoreApplication.translate("BNU_GYM", u"From", None))
        self.label_9.setText(QCoreApplication.translate("BNU_GYM", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("BNU_GYM", u"Tel", None))
        self.label_3.setText(QCoreApplication.translate("BNU_GYM", u"Pwd", None))
        self.label_2.setText(QCoreApplication.translate("BNU_GYM", u"Name", None))
        self.label_10.setText(QCoreApplication.translate("BNU_GYM", u"Rate", None))
        self.Name.setText("")
        self.label_11.setText(QCoreApplication.translate("BNU_GYM", u"\u672cApp\u4ec5\u4f9b\u5b66\u4e60\uff0c\u4e0d\u5f97\u7528\u4f5c\u5546\u4e1a\u76ee\u7684", None))
    # retranslateUi


def wait_until(hour:int=7,minute:int=29,second:int=0,check_freq=60):
    '''
    定时唤醒
    '''
    while True:
        now = datetime.now()
        print(now)
        if now.hour >= hour and now.minute >= minute and now.second >= second:
            break
        else:
            sleep(check_freq)
    return None

if __name__=="__main__":
    # 用QApplication创建应用实例
    app = QApplication(argv)
    ui = Ui_BNU_GYM()
    # # 船舰一个窗体类的对象，未设置
    # basewidget = QWidget()
    # # 加载定义的UI配置
    # ui = Ui_BNU_GYM()
    # # 用ui.setupUi创建 basewidget 上的组件
    # ui.setupUi(basewidget)
    # basewidget.show()

    wait_until(hour=7,minute=29,second=0)

    print('本文件为GUI,请运行`main.py`')


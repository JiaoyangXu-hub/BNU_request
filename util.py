import os
import re

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import zipfile


def unzip_file(src_file, dest_dir, *password):
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir, pwd=password)
    except RuntimeError as e:
        print(e)
    zf.close()


def check_chrome_driver():
    try:
        service = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    except Exception as msg:
        reg = "Current browser version is.+with"
        chrome_version = re.search(reg, str(msg)).group().replace("Current browser version is ", "").replace(" with","")
        file_name = 'chromedriver_' + chrome_version + '.zip'
        print("Chrome Version:" + chrome_version)

        url = 'https://registry.npmmirror.com/binary.html?path=chromedriver/' + chrome_version + '/chromedriver_win32.zip'
        response = requests.get(url=url)
        open(file_name, 'wb').write(response.content)
        # 解压zip文件
        unzip_file(file_name, '.')
        


check_chrome_driver()

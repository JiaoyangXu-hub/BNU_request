
from re import search
from urllib import request, response
from bs4 import BeautifulSoup
from requests import session
from des import PyJsHoisted_strEnc_
from paddleocr import PaddleOCR
from re import findall
from datetime import datetime

class Pipline:
    def __init__(self) -> None:
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        self.session = session()
        self.msg = ''
        self.ocr = PaddleOCR()

    def login(self,un,pd):
        self.msg = ''
        url = 'http://cas.bnu.edu.cn/cas/login?service=https%3A%2F%2Fcgyd.prsc.bnu.edu.cn%2Flogin.jsp'
        response = self.session.get(url=url,headers=self.header)
        if not response.status_code==200:
            self.msg += 'Login in html cant get \n'
        else:
            self.meg +  ''
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
        return res.status_code

    def get_free_space(self,item_type:str,start_datetime:datetime,end_datetime:datetime)->list:
        '''
        param:
            item_type:所抢球场类别可选(乒乓球,羽毛球,网球)
            start_datetime:开始时间
            end_datetime:截止时间
        return: [(date,id,begin_time,place),...]格式列表，错误则返回空列表
        '''
        param_d2s = 24*60*60
        item = {
            '乒乓球':'5462',
            '网球':'68788',
            '羽毛球':'5326',
        }
        # count how many day
        days = (start_datetime.timestamp()-end_datetime.timestamp())//param_d2s
        datetime.now().timestamp()
        if days>2:
            return []
        lst = []
        for i in range(days+1) :# TODO 做个并发
            time_date = datetime.fromtimestamp(start_datetime.timestamp()+i*(60*60*24)).strftime('%Y-%m-%d')
            response=self.session.get(
                url='https://cgyd.prsc.bnu.edu.cn/gymbook/gymBookAction.do',
                params={
                    'ms':'viewGymBook',
                    'gymnasium_id':'2',
                    'item_id':item[item_type],
                    'time_date':time_date,
                    'userType':'1',# 填1只有个表格，不填就是加载全部
                },
                headers=self.header,
            )
            response.encoding = response.apparent_encoding
            # soup = BeautifulSoup(response.text,'lxml')
            res_ptn = r"resourceArray\.push\(\{id:'([0-9]{4,5})',time_session:'(\d{1,2}):00-\d{1,2}:00',field_name:'(.+?)',overlaySize:'2',can_see_student:'',can_net_book:'1'\}\);"

            booked_ptn = r"markResStatus\('\d+?','(\d{4,5})','1'\);"
            resource_lst = findall(res_ptn,response.text)
            booked_lst = findall(booked_ptn,response.text)
            def in_trange(s):
                if (i == 0) and (int(s)*60*60 < start_datetime.timestamp()%param_d2s):
                    return False
                elif (i==days) and (int(s)*60*60 > end_datetime.timestamp()%param_d2s):
                    return False
                else:
                    return True

            lst.extend([(time_date,*res) for res in resource_lst if (res[0] not in booked_lst) and in_trange(res[1]) ]) # 没有订的空肠
        
        return lst
    
    def book_space(self,resource_lst:list,un:str,num:int=1,mod:int=1)-> bool:
        '''
        param:
            num : 预定个数 # TODO 注意还有是否连场，是否同一时间的判断
            resource_lst : Pipline.get_free_space的返回列表
            un : 学号
            mod : 模式 0:无倾向，1:倾向于选连续时间的场地，2:倾向于选同一时间的两个不同场地
        result: 是否成功
        '''
                # (date,id,begin_time,place)
        if num==2 and len(resource_lst)>=2:

            resource_lst.sort(key=lambda lst:(lst[0],lst[2],lst[3]))
            #TODO 功能有待完善
            # if mod==0 and len(resource_lst)>=2:

            #     self.msg += (' -- Order --\n'+'date\tid\ttime\tplace\n'+'\n'.join(['\t'.join(itm) for itm in resource_lst[0:2]])+'\n')
            # elif mod==1:
            #     for idx in range(max(0,len(resource_lst)-1)):
            #         if (int(resource_lst[idx+1][2])-int(resource_lst[idx][2])==1) and (resource_lst[idx+1][0]==resource_lst[idx][0]):
            #             resource_lst[idx:idx+2]
            #             break
            # elif mod==2:
            #     for idx in range(max(0,len(resource_lst)-1)):
            #         if (resource_lst[idx+1][0]==resource_lst[idx][0]) and (resource_lst[idx+1][2]==resource_lst[idx][2]):
            #             resource_lst[idx:idx+2]
            #             allFieldTime = 
            #             break
            # else:
            #     self.msg += 'mod error\n'

        elif num<=2 and len(resource_lst)==1: # 只有一个
            itm = resource_lst[0]
            allFieldTime = itm[1]+'#'+itm[0] #(date,id,begin_time,place)
        else:
            self.msg += 'num > 2 or mod error \n'
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
            'allFieldTime': allFieldTime,
            'companion_1': '(test)',# TODO 改成真名
            'companion_2': '',
            'companion_3': '',
            'companion_4': '',
            'companion_5': '',
            'companion_6': '',
            'companion_7': '',
            'companion_8': '',
            'companion_9': '',
            'checkcodeuser': self._checkcode(),
            'selectPayWay': '1',
        }
        resp = session.post(
            url='https://cgyd.prsc.bnu.edu.cn/gymbook/gymbook/gymBookAction.do?ms=saveGymBook',
            data=param,headers=self.header,
        )
        if findall('预定成功',resp.text):
            return True
        else:
            return False

    def _checkcode(self):
        '''
        采用paddleOCR识别和计算验证码的值
        若输入是字符串地址
        '''
        jpg = self.session.get(url='https://cgyd.prsc.bnu.edu.cn/Kaptcha.jpg',stream=True)
        path = './checkcode.jpg'
        if jpg.status_code==200:
            open(path,'wb').write(jpg.content)

        ocr_res = self.ocr(path,cls=False)[0][1]
        expre = findall(r'[0-9]{1,2}? *?[+-] *?[0-9]{1,2}',ocr_res[0])
        # 若识别匹配率到0.8以上且匹配到的pattern只有一个
        if ocr_res[1]>0.8 and len(expre)==1:
            return int(eval(expre[0]))  # 返回结果
        else:
            return float(ocr_res[1])    # 返回匹配识别率
        

    def get_checkcode(self):
        jpg = self.session.get(url='https://cgyd.prsc.bnu.edu.cn/Kaptcha.jpg',stream=True)
        if jpg.status_code==200:
            with open('checkcode.jpg','wb') as j:
                j.write(jpg.content)
        else:
            return

    def get_notice(self):
        '''
        获得场馆的通知
        '''
        return self.session.post(
            url='https://cgyd.prsc.bnu.edu.cn/gymbook/gymBookAction.do?ms=scanCgtz&gymnasium_id=2',
            headers=header,
            ).text
    def




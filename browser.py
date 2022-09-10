from des import PyJsHoisted_strEnc_

from requests import session,Response
from urllib.parse import quote
from bs4 import BeautifulSoup
from paddleocr import PaddleOCR
from datetime import datetime

{
    'header':{
        "code":0,
        "message":{
            "title":"",
            "detail":""
        }
    },
    'body':{
        'dataStores':{
            "975c5d1e-7b4b-49e9-98c7-59e2a912":{
                'rowSet':{
                    "primary":[{
                        "XM":"徐骄阳","_t":3,"XH":"202121250011","IS_LXS":"0","XBYX":"系统科学学院","LXDH":"16601296123","SSL":"4","SSH":"504","is_back":"当天返校","is_out":"不出京","sdate":"2022-09-02","edate":"2022-09-02","fenlei_TEXT":"实验科研（仅限前往南院、金丰和、文教园和小白楼等本校教学区）","fenlei":"SYKYNYJFH","CXYY":"南院","Sheng_TEXT":"北京市","Sheng":"北京市","Shi_TEXT":"北京市辖区","Shi":"北京市辖区","Qu_TEXT":"海淀区","Qu":"海淀区","JTDZ":"北太平庄","ZYJCRQ":" ","zhaiyao":"出校日期：2022-09-02;计划返校日期2022-09-02;是否当天返校：当天返校;是否出京：不出京;出校原因：SYKYNYJFH;外出地点：北京市北京市辖区海淀区北太平庄","count":"0",_o : {"XM":null,"XH":null,"IS_LXS":null,"XBYX":null,"LXDH":null,"SSL":null,"SSH":null,"is_back":null,"is_out":null,"sdate":null,"edate":null,"fenlei_TEXT":null,"fenlei":null,"CXYY":null,"Sheng_TEXT":null,"Sheng":null,"Shi_TEXT":null,"Shi":null,"Qu_TEXT":null,"Qu":null,"JTDZ":null,"ZYJCRQ":null,"zhaiyao":null,"count":null}}],
                    "filter":[],
                    "delete":[]
                    },
                'name':"975c5d1e-7b4b-49e9-98c7-59e2a912",
                'pageNumber':1,
                'pageSize':2147483647,
                'recordCount':1,
                'rowSetName':"d9bfad88-0adf-4ae9-9c76-345ed317",
                'parameters':{
                    "relatedcontrols":"body_0",
                    "primarykey":"pk_id",
                    "queryds":"975c5d1e-7b4b-49e9-98c7-59e2a912"
                }
            },
            "975c5d1e-7b4b-49e9-98c7-59e2a912_record":{
                'rowSet':{
                    "primary":[{
                        "JTDZ":"北太平庄",
                        "pk_id":"38e309a4:182d904f50a:-5a3a",
                        "Qu":"海淀区",
                        "is_back":"当天返校",
                        "CXYY":"南院",
                        "Sheng":"北京市",
                        "Shi":"北京市辖区",
                        "is_out":"不出京",
                        "fk_id":"2208262148328072",
                        "XBYX":"系统科学学院",
                        "Shi_TEXT":"北京市辖区",
                        "sdate":"1661443200000",
                        "Sheng_TEXT":"北京市",
                        "fenlei_TEXT":"实验科研（仅限前往南院、金丰和、文教园和小白楼等本校教学区）",
                        "count":"0",
                        "SSH":"504",
                        "Qu_TEXT":"海淀区",
                        "zhaiyao":"出校日期：2022-08-26;计划返校日期2022-08-26;是否当天返校：当天返校;是否出京：不出京;出校原因：SYKYNYJFH;外出地点：北京市北京市辖区海淀区北太平庄",
                        "ZYJCRQ":" ",
                        "SSL":"4",
                        "edate":"1661443200000",
                        "sdate_STR":"2022-08-26 00:00:00",
                        "XH":"202121250011",
                        "fenlei":"SYKYNYJFH",
                        "LXDH":"16601296123",
                        "XM":"徐骄阳",
                        "edate_STR":"2022-08-26 00:00:00",
                        "IS_LXS":"0"
                    }],
                    "filter":[],
                    "delete":[]
                },
                'name':"975c5d1e-7b4b-49e9-98c7-59e2a912_record",
                'pageNumber':1,
                'pageSize':2147483647,
                'recordCount':0,
                'rowSetName':"d9bfad88-0adf-4ae9-9c76-345ed317",
                'parameters':{
                    "exist":'true',
                    "relatedcontrols":"body_0",
                    "primarykey":"pk_id",
                    "queryds":"975c5d1e-7b4b-49e9-98c7-59e2a912"
                }
            },
            
            "variable":{
                'rowSet':{
                    "primary":[
                        {
                            "name":"count_white",
                            "source":"process",
                            "type":"string",
                            "value":"0",
                            "_t":1,
                            '_o' : {"value":""}
                        },{
                            "name":"出校区域",
                            "source":"process",
                            "type":"string",
                            "value":""
                        },{
                            "name":"服务摘要",
                            "source":"process",
                            "type":"string",
                            "value":"出校日期：2022-09-02;计划返校日期2022-09-02;是否当天返校：当天返校;是否出京：不出京;出校原因：SYKYNYJFH;外出地点：北京市北京市辖区海淀区北太平庄",
                            "_t":'1','_o' : {"value":""}
                        },{
                            "name":"BUSINESS_UNIT",
                            "source":"process",
                            "type":"string",
                            "value":""
                        },{
                            "name":"is_back",
                            "source":"process",
                            "type":"string",
                            "value":""
                        },{
                            "name":"is_out",
                            "source":"process",
                            "type":"string",
                            "value":""
                        },{
                            "name":"back",
                            "source":"process",
                            "type":"string",
                            "value":"当天返校",
                            "_t":'1','_o' : {"value":""}
                        },{
                            "name":"go",
                            "source":"process",
                            "type":"string",
                            "value":"不出京",
                            "_t":'1',
                            '_o' : {"value":""}
                        },{
                            "name":"出校原因",
                            "source":"process",
                            "type":"string",
                            "value":"实验科研（仅限前往南院、金丰和、文教园和小白楼等本校教学区）",
                            "_t":'1',
                            '_o' : {"value":""}
                        },{
                            "name":"is_shenhe",
                            "source":"process",
                            "type":"string",
                            "value":""
                        },{
                            "name":"选择出校原因",
                            "source":"process",
                            "type":"string",
                            "value":"SYKYNYJFH",
                            "_t":'1','_o' : {"value":""}
                        },{
                            "name":"外出地点","source":"process","type":"string","value":""
                        },{
                            "name":"IS_LXS","source":"process","type":"string","value":"0","_t":1,_o : {"value":""}
                        },{
                            "name":"SYS_USER","source":"interface","type":"string","value":"徐骄阳"
                        },{
                            "name":"SYS_UNIT","source":"interface","type":"string","value":"系统科学学院 "
                        },{
                            "name":"SYS_DATE","source":"interface","type":"date","value":"1662025939757"
                        },{
                            "name":"cec174df-1702-4095-aa0d-23a70283.ID_NUMBER","value":"202121250011"
                        },{
                            "name":"7100197524111360.N","value":"0"
                        },{
                            "name":"cec174df-1702-4095-aa0d-23a70283.UNIT_NAME","value":"系统科学学院"
                        },{
                            "name":"cec174df-1702-4095-aa0d-23a70283.MOBILE","value":""
                        },{
                            "name":"12727166118793216.COUNT(1)","value":"0"
                    }],
                    "filter":[],
                    "delete":[]
                },
                'name':"variable",
                'pageNumber':'1',
                'pageSize':'2147483647',
                'recordCount':'0',
                'parameters':{}
            },
            
            "uploader_0_record":{
                'rowSet':{
                    "primary":[{
                        "success":"true",
                        "result":"true",
                        "office_online":"false",
                        "web_office":"false",
                        "file_new_name":"263492bb49ce4f5d96ddc825748f.jpg",
                        "file_old_name":"xwud_8253258e9f9c386027fd64d94280b712.jpg",
                        "relative_path":"uploadfiles/serviceUpload/e87d2875-6fcf-4e6a-81bc-8ff99915aed3/2021/12/26/",
                        "file_size":"863","up_id":"fileupload_F756IJG9473EHSCS9FQTEM8T2"
                    }],
                    "filter":[],
                    "delete":[]
                },
                'name':"uploader_0_record",
                'pageNumber':'1',
                'pageSize':'2147483647',
                'recordCount':'0',
                'parameters':{}
            },
            "uploader_0":{
                'rowSet':{
                    "primary":[{
                        "div_name":"上传相关证明材料",
                        "div_id":"uploader_0",
                        "up_id":"fileupload_5RQ9943UJGPV3R461Q95TEKQF",
                        "file_size":"863",
                        "up_relative_path":"uploadfiles/serviceUpload/e87d2875-6fcf-4e6a-81bc-8ff99915aed3/2021/12/26/",
                        "up_file_new_name":"263492bb49ce4f5d96ddc825748f.jpg",
                        "up_newurl":"uploadfiles/serviceUpload/e87d2875-6fcf-4e6a-81bc-8ff99915aed3/2021/12/26/263492bb49ce4f5d96ddc825748f.jpg",
                        "up_encodeName":"xwud_8253258e9f9c386027fd64d94280b712.jpg",
                        "_t":1
                    }],
                    "filter":[],
                    "delete":[]
                },
                'name':"uploader_0",
                'pageNumber':'1',
                'pageSize':'2147483647',
                'recordCount':'0',
                'parameters':{"uploader":"true","exist":"true"}
            }
        },
        'parameters':{
            "formid":"acdedd90-b4de-4329-948d-380ce05a",
            "status":"select",
            "service_id":"e87d2875-6fcf-4e6a-81bc-8ff99915aed3",
            "process":"f9538769-1d7d-4acf-881d-3056d285790d",
            "seqId":"",
            "seqPid":"",
            "privilegeId":"9324195175f4f476cbfe4b8094985640",
            "record_fk":"2208262148328072",
            "strUserId":"",
            "strUserIdCC":"",
            "nextActId":""
        }
    }
}

class Browser(object):
    def __init__(self) -> None:
        self.session = session()
        self.session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        self.msg = ''
        self.ocr = PaddleOCR()

    def login(self,username:str,password:str) -> Response:
        '''
        网站登录
        ---
        params:
            username : 学号
            password : 密码
        return:
            POST返回的response,应当是https://one.bnu.edu.cn/这里
        '''
        url = 'https://cas.bnu.edu.cn/cas/login'
        response = self.session.get(url)
        if response.status_code != 200:
            raise ConnectionError('登录状态码非200')
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text,'lxml')
        lt = soup.select_one('#lt')['value']
        un = username
        pd = password
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
            url='http://cas.bnu.edu.cn/cas/login;jsessionid='+JSESSIONID,
            data=param,
        )
        return res

class Apply4Out(Browser):
    def __init__(self) -> None:
        super().__init__()
    def auto_apply4out(self):
        self.session.get()
        pass


if __name__=='__main__':
    browser = Browser()
    login_res = browser.login(username='202121250011',password='xysz402715')
    if login_res.status_code == 200:
        print('登录成功\n\n---------------\n\n')
        print(login_res.text)

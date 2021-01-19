# -*- encoding: utf-8 -*-
'''
@File    :   daka.py
@Time    :   2020/12/28 19:31:31
@Author  :   Geralt 
@Version :   1.0
@Contact :   superj0529@gmail.com
'''

# here put the import lib
import re
import sys
import urllib
from http import cookiejar

def getLt(response): 
    #获取流水号
    pattern = re.compile(r"LT-[0-9]*-[0-9a-zA-Z]*-tpass")
    lt = pattern.findall(response)[0]
    return lt

def getToken(response):
    #获取token
    pattern = re.compile(r"name=\"_token\"\s+value=\"([0-9a-zA-Z]+)\"")
    _token = pattern.findall(response)[0]
    return _token

def getName(response):
    #获取用户姓名
    pattern = re.compile(r"当前用户：\s*(\w+)\s*")
    name = pattern.findall(response)[0]
    return name

if __name__ == "__main__":
    cookie = cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    loginurl = "https://ehall.neu.edu.cn/infoplus/login?retUrl=https://ehall.neu.edu.cn/infoplus/form/JKXXSB/start"
    response1 = opener.open(loginurl)
    decode_txt1=response1.read().decode()
    lt = getLt(decode_txt1)
    id = sys.argv[1]
    password = sys.argv[2]
    values1 = {
        "_eventId":"submit",
        "execution":"e1s1",
        "lt":lt,
        "pl":str(len(password)),
        "rsa":id+password+lt,
        "ul":str(len(id))
    }
    postdata1 = urllib.parse.urlencode(values1).encode("utf-8")
    opener.addheaders = [("User-Agent",'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')]
    response2 = opener.open(response1.geturl(), postdata1)
    
    decode_txt2 = response2.read().decode()
    _token = getToken(decode_txt2)
    isForSelf = '1' if len(sys.argv)==3 else '0'
    name = sys.argv[4] if len(sys.argv)>3 else getName(decode_txt2)
    sid = id if len(sys.argv)==3 else sys.argv[3]
    
    formdata={
    '_token':_token,
    'cross_city':'无',
    'jiankangxinxi_muqianshentizhuangkuang':'正常',
    'jibenxinxi_shifoubenrenshangbao':isForSelf,
    'profile[suoshubanji]':'',
    'profile[xingming]':name,
    'profile[xuegonghao]':sid,
    'qitashixiang_qitaxuyaoshuomingdeshixiang':'',
    'xingchengxinxi_weizhishifouyoubianhua':'0',
    }
    postdata2 = urllib.parse.urlencode(formdata).encode("utf-8")
    response3 = opener.open('https://e-report.neu.edu.cn/api/notes', postdata2)
    print(response3.status)
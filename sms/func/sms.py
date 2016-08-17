#  -*- coding:UTF_8 -*-
import json
import requests

#请求的头部内容
headers={
    "X-LC-Id": "eYbcEdFl9PwvWvNUXKkckt2T-gzGzoHsz",
    "X-LC-Key": "I0z3BQPASuHWyUIHScv6CKd6",
    "Content-Type": "application/json",
}
# 请求发送验证码 API
REQUEST_SMS_CODE_URL='https://api.leancloud.cn/1.1/requestSmsCode'
#请求校验验证码 API
VERIFY_SMS_CODE_URL='https://api.leancloud.cn/1.1/verifySmsCode/'

def send_message(phone):
    '''
    通过post 请求 requestSmsCode API 发送验证码到指定手机
    :param phone:
    :return:
    '''
    data={
        'mobiePhoneNumber':phone,
    }
    r=requests.post(REQUEST_SMS_CODE_URL,data=json.dumps(data),headers=headers)
    if r.status_code==200:
        return True
    else:
        return  False

def verify(phone,code):
    target_url=VERIFY_SMS_CODE_URL + '%s?mobilePhoneNumber=%s'%(code,phone)
    r=requests.post(target_url,headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False
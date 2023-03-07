
from flask import Flask, render_template,request,Response,Blueprint
import json
import  api.sql as sql

import smtplib
import random
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

number=-3654842154

register_api = Blueprint('register_api', __name__)

@register_api.route('/api/register', methods=['POST'])
def register():
    info=request.get_json()
    email=info.get('email')
    pwd=info.get('pwd')
    check=info.get('check')
    res=sql.registercheck(email)
    global number

    if(res==-1):
        return json.dumps({'code':1,'msg':"error",'data':{'detail':'邮箱已存在'}})
    elif (res == 1):
        if (check != str(number)):
            return json.dumps({'code': 2, 'msg': "error", 'data': {'detail': '验证码错误'}})
        else :
            res=sql.register(email,pwd)
            if (res == 1) :
                return json.dumps({'code': 0, 'msg': "success", 'data': {'email':email,'name':email,'token': '135456user'}})
            else:
                return json.dumps({'code': 4, 'msg': "error", 'data': {'detail': '其他错误'}})
    else:
        return json.dumps({'code': 4, 'msg': "error", 'data': {'detail': '其他错误'}})

send_api = Blueprint('send_api', __name__)

@send_api.route('/api/getemail', methods=['POST'])
def send():
    info = request.get_json()
    email = info.get('email')
    res = sql.registercheck(email)
    
    if (res == -1):
        return json.dumps({'code': 1, 'msg': "error", 'data': {'detail': '邮箱已存在'}})
    # 用于构建邮件头
    # 发信方的信息：发信邮箱，126 邮箱授权码
    from_addr = 'echrra@163.com'
    password = 'KKNGEFKHXKNNNIJN'

    # 收信方邮箱
    to_addr = email

    # 发信服务器
    smtp_server = 'smtp.163.com'
    global number
    number = random.randint(10000, 99999)
    """标题"""
    head = "邮箱验证码"
    """正文"""
    text = "【心印】您的验证码"+str(number)+"，该验证码5分钟内有效，请勿泄漏于他人！"

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(text, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(head)

    # 开启发信服务，这里使用的是加密传输
    # server = smtplib.SMTP_SSL()
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()

    return Response(json.dumps({'code': 1000, 'msg': "success", 'data': {'detail': '成功'}}))
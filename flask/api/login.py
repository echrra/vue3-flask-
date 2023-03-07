from flask import Flask, render_template,request,Response,Blueprint
import json
import  api.sql as sql


login_api = Blueprint('login_api', __name__)

@login_api.route('/api/login', methods=['POST'])
def login():
    info=request.get_json()
    email=info.get('email')
    pwd=info.get('pwd')
    res,name=sql.logincheck(email,pwd)
    if(res==1):
        return json.dumps({'code':0,'msg':"success",'data':{'email':email,'name':name,'token':'135456user'}})
    elif(res==-1):
        return json.dumps({'code':1,'msg':"error",'data':{'detail':'邮箱不存在'}})
    elif (res== -2):
        return json.dumps({'code': 2, 'msg': "error", 'data': {'detail': '密码错误'}})
    else:
        return json.dumps({'code': 4, 'msg': "error", 'data': {'detail': '其他错误'}})

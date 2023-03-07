from flask import Flask, render_template,request,Response
import json
from flask_cors import *

import  api.sql as sql

from api.login import login_api
from api.register import  register_api,send_api
from api.get import getallemail_api,getgenre_api,getsearch_api,getcomment_api,getrecommend_api
app=Flask(__name__, static_url_path='')

#CORS(app, supports_credentials=True)

@app.after_request
def cors(resp):
    resp.headers.add('Access-Control-Allow-Origin','http://81.68.113.102')
    resp.headers.add('Access-Control-Allow-Headers','x-requested-with,content-type')
    resp.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE')
    resp.headers.add("Access-Control-Allow-Credentials", "true");
    return resp


app.register_blueprint(login_api)
app.register_blueprint(register_api)
app.register_blueprint(send_api)
app.register_blueprint(getallemail_api)
app.register_blueprint(getgenre_api)
app.register_blueprint(getsearch_api)
app.register_blueprint(getcomment_api)
app.register_blueprint(getrecommend_api)

if __name__ == '__main__':
    app.debug = False
    app.run(host="81.68.113.102", port="8080")
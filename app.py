# from crypt import methods
from importlib.resources import Resource
import re
from flask import render_template,Flask,request
from flask_cors import *
import mysql
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

sql = mysql.Mysql()
#注册接口
@app.route("/register",methods=['POST'])
def register():
    if request.method == 'POST':
        re = json.loads(request.data)
        #print(re['username'])
        username = re['username']
        password = re['password']
        # print(username)
        # print(password)
        #sql = mysql.Mysql()
        sql.insert_sql(username,password)
        
        #re = request.data['message']

        #print(re)
        
    return '注册成功'
    #return render_template('index.html')


#登录接口
@app.route("/login",methods=['POST'])
def login():
    if request.method == 'POST':
        username = re['username']
        password = re['password']
        #sql = mysql.Mysql()
        ans = sql.select_user(username,password)
        if ans == 1:
            return '1'
        else:
            return '0'

#查询接口
@app.route('/select',methods = ['POST'])
def select():
    if request.method == 'POST':
        school_name = request.args['school_name']#获取搜索参数
        #print(school_name)
        result = sql.select_school(school_name = school_name)
        #return '1'
        return json.dumps(result)
    #pass
#插入接口
@app.route('/ins',methods = ['POST'])
def ins():
    if request.method == 'POST':
        SchoolName = request.args['SchoolName']#获取插入数据参数
        result = sql.insert_school(SchoolName)
        return result



if __name__ == '__main__':

    app.run(host='0.0.0.0',port='5000',debug=True)
    
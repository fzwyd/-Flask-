from flask import Flask,render_template,request
import mysql

app = Flask(__name__)

@app.route('/login',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        # print(name, password)
        # sql.insert_sql(username = name, password= password)
        result = sql.select_user(name,password)
        if result == 1:
            print(result)
            return render_template('home.html')
        else:
            print(result)
            return render_template('error.html')
        # return 'this is post'

if __name__ == '__main__':
    sql = mysql.Mysql()
    sql.create_sql()
    app.run()




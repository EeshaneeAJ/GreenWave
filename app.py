from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='952003'
app.config['MYSQL_DB']='green_wave'
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def sign():
    if request.method== 'POST':
        userDetails=request.form
        username=userDetails['username']
        name=userDetails['name']
        email=userDetails['email']
        password=userDetails['password']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO sign_up(username,name,email,password)VALUES(%s,%s,%s,%s)",(username,name,email,password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('sign.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method== 'POST':
        userDetails=request.form
        username=userDetails['username']
        password=userDetails['password']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO login(username,password)VALUES(%s,%s)",(username,password))
        mysql.connection.commit()
        cur.close()
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)
    
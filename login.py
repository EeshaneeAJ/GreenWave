from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='My_Sql101'
app.config['MYSQL_DB']='green_wave'
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def login():
    if request.method== 'POST':
        userDetails=request.form
        username=userDetails['username']
        password=userDetails['password']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO login(username,password)VALUES(%s,%s)",(username,password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)
    
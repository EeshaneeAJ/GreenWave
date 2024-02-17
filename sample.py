from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='952003'
app.config['MYSQL_DB']='himaja'
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method== 'POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email)VALUES(%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
    
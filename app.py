from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
import MySQLdb
app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='My_Sql101'
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
        return redirect(url_for('events'))
    return render_template('login.html')
@app.route('/events')
def events():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    cursor.close()
    return render_template('events.html', events=events)
@app.route('/redirect_to_post')
def redirect_to_post():
    return redirect(url_for('post'))

def events():
    conn = mysql.connection
    cursor = conn.cursor()
@app.route('/post',methods=['GET','POST'])
def post():
    if request.method== 'POST':
        userDetails=request.form
        post=userDetails['post']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO post_message(post)VALUES(%s)",(post,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('likes'))
    return render_template('post.html')
@app.route('/likes',methods=['GET','POST'])
def likes():
    conn = MySQLdb.connect(host='localhost', user='root', password='My_Sql101', database='green_wave')
    cur = conn.cursor()
    cur.execute("SELECT post FROM post_message")
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('likes.html', posts=posts)
if __name__ == '__main__':
    app.run(debug=True)
    
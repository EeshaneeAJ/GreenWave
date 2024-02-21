from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
import MySQLdb
app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='952003'
app.config['MYSQL_DB']='green_wave'
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/sign',methods=['GET','POST'])
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
@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':
        registration_details = request.form
        username = registration_details['username']
        event_name = registration_details['event_name']
        name = registration_details['name']
        address = registration_details['address']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO registration (username, event_name, name, address) VALUES (%s, %s, %s, %s)",
                    (username, event_name, name, address))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('post'))
    if request.method == 'GET':
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM events")
        events = cursor.fetchall()
        cursor.close()
        return render_template('events.html', events=events)
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
@app.route('/likes', methods=['GET', 'POST'])
def likes():
    if request.method == 'POST':
        # Process comment submission
        comments_details = request.form
        post_id = comments_details['post_id']
        comment = comments_details['comment']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO comments(post_id, comment) VALUES (%s, %s)", (post_id, comment))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('likes'))

    elif request.method == 'GET':
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM post_message")
        posts = cursor.fetchall()
        cursor.close()
        return render_template('likes.html', posts=posts)

@app.route('/footprint1')
def footprint1():
   return render_template('footprint1.html')
@app.route('/footprint2', methods=['GET', 'POST'])
def footprint2():
    if request.method == 'POST':
        country = request.form['country']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM footprint WHERE country = %s", (country,))
        data = cur.fetchone()
        cur.close()
        if data:
            # Fetch column names separately
            cur = mysql.connection.cursor()
            cur.execute("SHOW COLUMNS FROM footprint")
            column_names = [column[0] for column in cur.fetchall()]
            cur.close()

            # Create a dictionary with column names as keys and data values as values
            data_dict = dict(zip(column_names, data))

            return render_template('footprint2.html', data=data_dict)
        else:
            flash(f"No data found for the country: {country}")
            return redirect(url_for('footprint1'))
    return render_template('footprint2.html')


if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'loginweb'
mysql = MySQL(app)

@app.route('/')
def hello():
    return 'welcome to user login tuts'


@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'GET':
        return render_template('registrasi.html')
    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO accounts(username, email, password) VALUES(%s,%s,%s)''',(username, email, password))
        mysql.connection.commit()
        cursor.close()
        flash('Data added successfully','success')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        # Check if "username" and "password" POST requests exist (user submitted form)
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            # Create variables for easy access
            email = request.form['email']
            password = request.form['password']

            
            # get username and password from db 
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password))

            user = cursor.fetchone()

            if user:
                session['logged_in'] = True
                session['email'] = user[3]

                flash('Login successful','success')
                cursor.close()
                return redirect(url_for('dashboard'))
                # return render_template('dashboard.html', user=user)

            else:
                flash('Invalid username/password','danger')
            
            
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    flash('Logout successful','success')
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

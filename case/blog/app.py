from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blog'
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

        # encrypt password
        password = hashlib.md5(password.encode())

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO authors(username, email, password) VALUES(%s,%s,%s)''',(username, email, password.hexdigest()))
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

             # encrypt password
            password = hashlib.md5(password.encode())
            
            # get username and password from db 
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM authors WHERE email = %s AND password = %s', (email, password.hexdigest()))

            user = cursor.fetchone()

            if user:
                session['logged_in'] = True
                session['id'] = user[0]
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
    cursor = mysql.connection.cursor()
    cursor.execute('''
        SELECT id_art, title, username, name_cat, datetime 
        FROM articles 
        INNER JOIN authors ON articles.author = AUTHORS.id_author 
        INNER JOIN categories ON articles.category = categories.id_cat
        ORDER BY datetime DESC
    ''')

    articles = cursor.fetchall()
    return render_template('dashboard.html', articles=articles)

@app.route('/artikel', methods=['GET', 'POST'])
def artikel():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('''
            SELECT * FROM categories
        ''')

        categories = cursor.fetchall()

        cursor.close()
        return render_template('artikel/tambah.html', categories=categories)
    else:
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO articles(title, description, category, author, datetime) VALUES(%s,%s,%s,%s,now())''',(title, description, category, session['id']))
        mysql.connection.commit()
        cursor.close()
        flash('Data added successfully','success')
        return redirect(url_for('dashboard'))

@app.route('/artikel/edit/<int:id>', methods=['GET', 'POST'])
def editdosen(id):
    if request.method == 'GET':


        cursor = mysql.connection.cursor()
        cursor.execute('''
        SELECT id_art, title, description, name_cat, id_cat
        FROM articles 
        INNER JOIN authors ON articles.author = AUTHORS.id_author 
        INNER JOIN categories ON articles.category = categories.id_cat
        WHERE id_art=%s''', (id, ))
        artikel = cursor.fetchone()

        cursor.execute('''
            SELECT * FROM categories
        ''')
        categories = cursor.fetchall()
        cursor.close()

        return render_template('artikel/edit.html', artikel=artikel, categories=categories)
    else:
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']

        cursor = mysql.connection.cursor()
        cursor.execute('''
        UPDATE articles  
        SET
            title = %s,
            description = %s,
            category = %s
        WHERE
            id_art = %s;
        ''',(title,description,category,id))

        mysql.connection.commit()
        cursor.close()
        flash('Data updated successfully','success')
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html')

@app.route('/artikel/delete/<int:id>', methods=['GET'])
def deletedosen(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('''
        DELETE
        FROM articles
        WHERE id_art=%s''', (id, ))
        mysql.connection.commit()
        cursor.close()
        flash('data deleted','success')
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('email', None)
    flash('Logout successful','success')
    return redirect(url_for('login'))
    

#------------ tampilan depan 
@app.route('/front')
def front():
    cursor = mysql.connection.cursor()
    cursor.execute('''
        SELECT id_art, title, username, name_cat, datetime, description
        FROM articles 
        INNER JOIN authors ON articles.author = AUTHORS.id_author 
        INNER JOIN categories ON articles.category = categories.id_cat
        ORDER BY datetime DESC
    ''')

    articles = cursor.fetchall()
    return render_template('front.html', articles=articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

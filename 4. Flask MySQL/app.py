from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'universitas'
mysql = MySQL(app)

@app.route('/hello/<nama>')
def hello(nama):
    return render_template('hello.html', nama=nama)

@app.route('/dosen')
def dosen():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM DOSEN")
    dosen = cursor.fetchall()
    cursor.close()

    return render_template('dosen.html', dosen=dosen)

@app.route('/dosen/tambah', methods=['GET', 'POST'])
def tambahdosen():
    if request.method == 'GET':
        return render_template('dosen/add.html')
    else:
        nama = request.form['nama']
        univ = request.form['univ']
        jurusan = request.form['jurusan']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO dosen(nama,univ,jurusan) VALUES(%s,%s,%s)''',(nama,univ,jurusan))
        mysql.connection.commit()
        cursor.close()
        flash('Data added successfully','success')
        return redirect(url_for('dosen'))

    return render_template('dosen.html')

@app.route('/dosen/edit/<int:id>', methods=['GET', 'POST'])
def editdosen(id):
    if request.method == 'GET':

        cursor = mysql.connection.cursor()
        cursor.execute('''
        SELECT *
        FROM DOSEN
        WHERE dosen_id=%s''', (id, ))
        dosen = cursor.fetchone()
        cursor.close()

        return render_template('dosen/edit.html', dosen=dosen)
    else:
        nama = request.form['nama']
        univ = request.form['univ']
        jurusan = request.form['jurusan']

        cursor = mysql.connection.cursor()
        cursor.execute('''
        UPDATE dosen
        SET
            nama = %s,
            univ = %s,
            jurusan = %s
        WHERE
            dosen_id = %s;
        ''',(nama,univ,jurusan,id))

        mysql.connection.commit()
        cursor.close()
        flash('Data updated successfully','success')
        return redirect(url_for('dosen'))

    return render_template('dosen.html')

@app.route('/dosen/delete/<int:id>', methods=['GET'])
def deletedosen(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('''
        DELETE
        FROM DOSEN
        WHERE dosen_id=%s''', (id, ))
        mysql.connection.commit()
        cursor.close()
        flash('dosen deleted','success')
        return redirect(url_for('dosen'))

    return render_template('dosen.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        if request.form['username'] != 'faqih@gmail.com' or request.form['password'] != 'userganteng':
            flash('Invalid username/password','danger')
        else:
            session['logged_in'] = True
            flash('Login successful','success')
            return redirect(url_for('dosen'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout successful','success')
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

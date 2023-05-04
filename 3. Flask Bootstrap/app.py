from flask import Flask, render_template, url_for, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

@app.route('/hello/<nama>')
def hello(nama):
    return render_template('hello.html', nama=nama)

@app.route('/dosen')
def dosen():
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

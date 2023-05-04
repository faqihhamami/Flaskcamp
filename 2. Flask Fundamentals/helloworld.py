from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return 'Ini adalah halaman about'

@app.route('/user/<int:id>')
def user(id):
    return f'hello selamat datang user {id}'

@app.route('/users/<string:nama>')
def users(nama):
    return render_template('users.html', user=nama)

@app.route('/students')
def students():
    users = ['Dani', 'Toni', 'Andi']
    return render_template('students.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

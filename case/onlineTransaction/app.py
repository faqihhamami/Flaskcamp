from flask import Flask, render_template, url_for, redirect, request, session, flash, jsonify
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
def hello_world():
    return 'welcome to toko online'

@app.route('/buy', methods=['POST', 'GET'])
def buy():
    if request.method == 'GET':
        return render_template('formtransaction.html')
    else:
        products = request.form.getlist('product[]')
        prices = request.form.getlist('price[]')
        qtys = request.form.getlist('qty[]')

        # return jsonify(qtys)
        #  insert to db
        for product, price, qty in zip(products, prices, qtys):
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO transaction(product, price, qty) VALUES(%s,%s,%s)''',([product], [price], [qty]))
            mysql.connection.commit()
        cursor.close()

        return redirect(url_for('dash'))

@app.route('/dash', methods=['POST', 'GET'])
def dash():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM transaction order by id desc")
    alltransaction = cursor.fetchall()
    cursor.close()

    return render_template('dash.html', alltransaction=alltransaction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

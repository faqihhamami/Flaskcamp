from flask import Flask, render_template, url_for, redirect, request, session, flash, jsonify
from flask_mysqldb import MySQL
from random import randint
# import pywhatkit as w
from datetime import datetime


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
    return 'welcome to static transaction'


@app.route('/transaction')
def transaction():
    # get payment methods
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM payment")
    payment = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product")
    theproduct = cursor.fetchall()


    products = ["product"+str(i) for i in range(3)]
    prices = ["price"+str(i) for i in range(3)]
    qtys = ["qty"+str(i) for i in range(3)]

    trans = zip(products, prices, qtys)

    cursor.close()

    return render_template('transaction.html', trans=trans, payment=payment, theproduct=theproduct)
    
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
   if request.method == 'POST':
    # get buyer and category
    buyer = request.form['buyer']
    category = request.form['category']

    products = [request.form[f'product{i}'] for i in range(3)]
    prices = [request.form[f'price{i}'] for i in range(3)]
    qtys = [request.form[f'qty{i}'] for i in range(3)]

    # sum total 
    total = 0

    for price, qty in zip(prices, qtys):
        total = total + (int(price) * int(qty))

    # return jsonify(total)
    # return redirect(url_for('checkout', total=total, detail=zip(products,prices,qtys)))
    return render_template('checkout.html', buyer=buyer, category=category, total=total, detail=zip(products,prices,qtys))


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        buyer = request.form['buyer']
        category = request.form['category']

        products = request.form.getlist('product[]')
        prices = request.form.getlist('price[]')
        qtys = request.form.getlist('qty[]')

        # generate invoice 8 digits
        invoicenumber = randint(10000000, 99999999) 
        
        # get total 
        total = 0
        # return jsonify(qty)

        # #  insert to detailtransaction table
        for product, price, qty in zip(products, prices, qtys):
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO _detailtransaction(product, price, qty, invoicenumber) VALUES(%s,%s,%s,%s)''',([product], [price], [qty], invoicenumber))

            # get  total 
            total = total + (int(price) * int(qty))
            mysql.connection.commit()
        
        # insert to singletransaction table
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO _singletransaction(invoicenumber, buyer, payment, total) VALUES(%s,%s,%s,%s)''',(invoicenumber, buyer, category,total))

        mysql.connection.commit()

        cursor.close()
        
        
        return redirect(url_for('transaction'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

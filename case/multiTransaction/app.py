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
    return 'welcome to toko online'

@app.route('/buy', methods=['POST', 'GET'])
def buy():
    if request.method == 'GET':

        # get payment methods
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM payment")
        payment = cursor.fetchall()
        cursor.close()

        return render_template('formtransaction.html', payment=payment)
    else:
        # get indentity and payment
        buyer = request.form['buyer']
        category = request.form['category']

        # get selected products 
        products = request.form.getlist('product[]')
        prices = request.form.getlist('price[]')
        qtys = request.form.getlist('qty[]')

        # get total = prices * qtys 
        total = 0

        # generate invoice 8 digits
        invoicenumber = randint(10000000, 99999999) 
        
        # #  insert to detailtransaction table
        for product, price, qty in zip(products, prices, qtys):
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO detailtransaction(product, price, qty, invoicenumber) VALUES(%s,%s,%s,%s)''',([product], [price], [qty], invoicenumber))

            # get  total 
            total = total + (int(price) * int(qty))
            mysql.connection.commit()
        
        # return jsonify(total)
        # insert to singletransaction table
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO singletransaction(invoicenumber, buyer, payment, total) VALUES(%s,%s,%s,%s)''',(invoicenumber, buyer, category,total))

        mysql.connection.commit()

        cursor.close()
        
        # get hour and minute 
        now = datetime.now()
        h = now.hour
        m = now.minute

        # send to wa  - install pywhatkit 5.4
        import pywhatkit as w
        note = f'No Invoice {invoicenumber} \nAnda telah membeli {products} \nTotal belanja adalah {total}'
        # w.sendwhatmsg("+6281563725902", str(note) ,h,m+2)
        w.sendwhatmsg("+6287888222025", str(note) ,h,m+2)
        
        return redirect(url_for('dash'))

@app.route('/dash', methods=['POST', 'GET'])
def dash():
    cursor = mysql.connection.cursor()
    cursor.execute('''
    SELECT * 
    FROM singletransaction 
    INNER JOIN payment
    ON singletransaction.payment = payment.id_payment
    order by id desc
    ''')
    alltransaction = cursor.fetchall()
    cursor.close()

    return render_template('dash.html', alltransaction=alltransaction)

@app.route('/detail/<int:number>', methods=['POST', 'GET'])
def detail(number):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM detailtransaction where invoicenumber = %s",(number, ))
    detail = cursor.fetchall()
    cursor.close()

    return render_template('detail.html', detail=detail)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

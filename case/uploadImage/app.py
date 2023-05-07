from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blog'
mysql = MySQL(app)

# image config 
app.config['UPLOAD_FOLDER'] = 'uploads/'


# https://thinkinfi.com/upload-and-display-image-in-flask-python/
# https://www.geeksforgeeks.org/how-to-upload-file-in-python-flask/
# https://medium.com/featurepreneur/uploading-files-using-flask-ec9fb4c7d438

@app.route('/')
def hello():
    return 'welcome to upload images'

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(secure_filename(f.filename))
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        return 'file uploaded'
    else:
        return render_template('galery.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)

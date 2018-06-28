from flask import send_from_directory
from flask import Flask, render_template, request, session, redirect, url_for
from flask import make_response
import os

from werkzeug.utils import secure_filename
UPLOAD_FOLDER = os.getcwd() + "/uploads"

app = Flask(__name__)

app.secret_key = 'frase para criptografar'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        is_logged = True
        name = session['username']
    else:
        is_logged = False
        name = 'nada'
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    arquivos = os.listdir(UPLOAD_FOLDER)
            
    rendered = render_template('index.html',is_logged = is_logged, name = name, arquivos = arquivos)
    return rendered


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

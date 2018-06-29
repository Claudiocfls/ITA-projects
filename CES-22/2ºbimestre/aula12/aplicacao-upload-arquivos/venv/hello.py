from flask import Flask, render_template, request
from flask import make_response
app = Flask(__name__)


@app.route('/')
def index():
    qtd_visitas = request.cookies.get('qtdVis')
    if not qtd_visitas:
        qtd_visitas = 1
    else:
        qtd_visitas = int(qtd_visitas) + 1

    rendered = render_template('index.html',qtd_visitas=qtd_visitas)
    resp = make_response(rendered)
    resp.set_cookie('qtdVis', str(qtd_visitas), max_age=60*2)
    return resp


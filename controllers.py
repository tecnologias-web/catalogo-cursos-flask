from app import app
from database.funcoes import obter_curso_por_sigla, listar_disciplinas_por_sigla
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/entrar')
def entrar():
    return render_template('entrar.html')


@app.route('/cursos/ads')
def curso_ads():
    curso_ads = obter_curso_por_sigla('ads')
    disciplinas = listar_disciplinas_por_sigla('ads')
    return render_template(
        'curso.html',
        curso=curso_ads,
        disciplinas=disciplinas
    )

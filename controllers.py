from app import app
from database.classes import Curso, Disciplina, Premio
from flask import render_template


@app.route('/')
def index():
    return render_template(
        'index.html',
        premios=Premio.listar()
    )


@app.route('/sobre')
def sobre():
    return render_template(
        'sobre.html'
    )


@app.route('/entrar')
def entrar():
    return render_template(
        'entrar.html'
    )


@app.route('/contato')
def contato():
    return render_template(
        'contato.html'
    )


@app.route('/cursos/ads')
def cursos():
    objeto = Curso.obter('ads')
    disciplinas = Disciplina.filtrar(objeto.sigla)
    return render_template(
        'curso.html',
        curso=objeto,
        disciplinas=disciplinas
    )


@app.context_processor
def listar_cursos():
    return dict(cursos_menu=Curso.listar())

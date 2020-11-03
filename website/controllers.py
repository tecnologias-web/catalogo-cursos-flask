from database.classes import Curso, Disciplina, Premio
from flask import Blueprint, render_template


website_bp = Blueprint(
    'website',
    __name__,
    template_folder='templates'
)


@website_bp.route('/')
def index():
    return render_template(
        'index.html',
        premios=Premio.listar()
    )


@website_bp.route('/sobre')
def sobre():
    return render_template(
        'sobre.html'
    )


@website_bp.route('/entrar')
def entrar():
    return render_template(
        'entrar.html'
    )


@website_bp.route('/contato')
def contato():
    return render_template(
        'contato.html'
    )


@website_bp.route('/cursos/<sigla>')
def cursos(sigla):
    objeto = Curso.obter(sigla)
    disciplinas = Disciplina.filtrar(objeto.sigla)
    return render_template(
        'curso.html',
        curso=objeto,
        disciplinas=disciplinas
    )


@website_bp.context_processor
def listar_cursos():
    return dict(cursos_menu=Curso.listar())

from datetime import datetime
from database.classes import Curso, Disciplina, Premio, Usuario
from flask import Blueprint, flash, redirect, render_template, request, session


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


@website_bp.route('/autenticar', methods=['POST'])
def autenticar():
    form = request.form
    usuario = Usuario.autenticar(
        form.get('usuario'),
        form.get('senha')
    )
    if usuario:
        session['usuario'] = usuario.nome
        session['data'] = datetime.now().__str__()
        return redirect('/admin')
    else:
        flash('Usuário ou senha incorretos!')
        return redirect('/entrar')


@website_bp.route('/sair')
def sair():
    session.clear()
    return redirect('/')


@website_bp.route('/contato', methods=['GET', 'POST'])
def contato():

    if request.method == 'POST':
        form = request.form
        print(f'''
        ++++ MENSAGEM ENVIADA ++++
        -> Nome: {form.get('nome')}
        -> E-mail: {form.get('email')}
        -> Assunto: {form.get('assunto')}
        -> Como Conheceu: {form.get('conheceu')}
        -> Mensagem:
        {form.get('mensagem')}
        ''')

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

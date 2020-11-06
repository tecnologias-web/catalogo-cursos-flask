from flask import Blueprint, redirect, request, render_template, session
from database.classes import Curso

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates'
)


@admin_bp.route('/')
def home():
    if 'usuario' not in session:
        return redirect('/entrar')
    return render_template('admin/home.html')


@admin_bp.route('/cursos')
def cursos():
    if 'usuario' not in session:
        return redirect('/entrar')
    return render_template(
        'admin/cursos.html',
        cursos=Curso.listar()
    )


@admin_bp.route('/cursos/criar', methods=['GET', 'POST'])
def cursos_criar():
    if 'usuario' not in session:
        return redirect('/entrar')
    curso = {}
    erros = []
    if request.method == 'POST':
        curso = request.form
        erros = Curso.criar(
            curso.get('nome'),
            curso.get('sigla'),
            curso.get('tipo'),
            curso.get('descricao'),
            curso.get('coordenador'),
            int(curso.get('duracao')),
            curso.get('diurno') == 'S',
            curso.get('noturno') == 'S'
        )

        if len(erros) == 0:
            return redirect('/admin/cursos')

    return render_template(
        'admin/cursos_form.html',
        curso=curso,
        titulo='Novo Curso',
        erros=erros
    )


@admin_bp.route('/cursos/alterar/<sigla>', methods=['GET', 'POST'])
def cursos_alterar(sigla):
    if 'usuario' not in session:
        return redirect('/entrar')
    curso = Curso.obter(sigla)
    erros = []
    if request.method == 'POST':
        curso = request.form
        erros = Curso.alterar(
            curso.get('nome'),
            curso.get('sigla'),
            curso.get('tipo'),
            curso.get('descricao'),
            curso.get('coordenador'),
            int(curso.get('duracao')),
            curso.get('diurno') == 'S',
            curso.get('noturno') == 'S'
        )

        if len(erros) == 0:
            return redirect('/admin/cursos')

    return render_template(
        'admin/cursos_form.html',
        curso=curso,
        titulo=f'Alterar {curso.sigla}',
        erros=erros
    )


@admin_bp.route('/cursos/remover/<sigla>', methods=['POST'])
def cursos_remover(sigla):
    if 'usuario' not in session:
        return redirect('/entrar')
    Curso.remover(sigla)
    return redirect('/admin/cursos')

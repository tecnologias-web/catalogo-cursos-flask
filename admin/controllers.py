from flask import Blueprint, jsonify, redirect, request, render_template
from database.classes import Curso
from admin.decorators import login_required


admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates'
)


@admin_bp.route('/')
@login_required
def home():
    return render_template('admin/home.html')


@admin_bp.route('/cursos')
@login_required
def cursos():
    return render_template(
        'admin/cursos.html',
        cursos=Curso.listar()
    )


@admin_bp.route('/cursos/criar', methods=['GET', 'POST'])
@login_required
def cursos_criar():
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
@login_required
def cursos_alterar(sigla):
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
@login_required
def cursos_remover(sigla):
    Curso.remover(sigla)
    return redirect('/admin/cursos')


@admin_bp.route('/cursos/verificar/<sigla>')
@login_required
def cursos_verificar(sigla):
    curso = Curso.obter(sigla)
    resultado = {}
    if not curso:
        resultado['existe'] = False
    else:
        resultado['existe'] = True
        resultado['mensagem'] = f'Sigla {sigla} já em uso'
    return jsonify(resultado)

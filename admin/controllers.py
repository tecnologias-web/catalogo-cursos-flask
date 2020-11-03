from flask import Blueprint, render_template
from database.classes import Curso

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates'
)


@admin_bp.route('/')
def home():
    return render_template('admin/home.html')


@admin_bp.route('/cursos')
def cursos():
    return render_template(
        'admin/cursos.html',
        cursos=Curso.listar()
    )

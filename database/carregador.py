import json
import os

from database.classes import Curso, Disciplina, Premio


def carregar_dados(base_dir):
    with open(os.path.join(base_dir, 'dados.json')) as json_arq:
        dados = json.load(json_arq)
        carregar_cursos(dados['cursos'])
        carregar_disciplinas(dados['disciplinas'])
        carregar_premios(dados['premios'])


def carregar_cursos(cursos):
    for curso in cursos:
        Curso.criar(
            curso['nome'],
            curso['sigla'],
            curso['tipo'],
            curso['descricao'],
            curso['coordenador'],
            curso['duracao'],
            curso['diurno'],
            curso['noturno']
        )
    print(f'Carregados {len(cursos)} cursos com sucesso!')


def carregar_disciplinas(disciplinas):
    for disciplina in disciplinas:
        Disciplina.criar(
            disciplina['nome'],
            Curso.obter(disciplina['curso']),
            disciplina['semestre'],
            disciplina['presencial'],
            disciplina['ead']
        )
    print(f'Carregados {len(disciplinas)} disciplinas com sucesso!')


def carregar_premios(premios):
    for premio in premios:
        Premio.criar(
            premio['titulo'],
            premio['descricao'],
            Curso.obter(premio['curso'])
        )
    print(f'Carregados {len(premios)} prêmios com sucesso!')


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    carregar_dados(base_dir)

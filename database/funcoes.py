from .dados import CURSOS, DISCIPLINAS


def obter_curso_por_sigla(sigla=''):
    for curso in CURSOS:
        if curso['sigla'].lower() == sigla.lower():
            return curso


def listar_disciplinas_por_sigla(sigla=''):
    lista = []
    for discip in DISCIPLINAS:
        if discip['curso'].lower() == sigla.lower():
            lista.append(discip)
    return lista

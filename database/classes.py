class Curso(object):

    __dados = []

    def __init__(self, nome, sigla, tipo, descricao, coordenador,
                 duracao, diurno, noturno):
        self.nome = nome
        self.sigla = sigla
        self.tipo = tipo
        self.descricao = descricao
        self.coordenador = coordenador
        self.duracao = duracao
        self.diurno = diurno
        self.noturno = noturno

    def __str__(self):
        return f'{self.sigla} - {self.nome}'

    @classmethod
    def criar(cls, nome, sigla, tipo, descricao, coordenador,
              duracao, diurno, noturno):
        Curso.__dados.append(
            cls(nome, sigla, tipo, descricao, coordenador,
                duracao, diurno, noturno)
        )

    @classmethod
    def obter(cls, sigla):
        for c in Curso.__dados:
            if c.sigla.lower() == sigla.lower():
                return c

    @classmethod
    def listar(cls):
        return Curso.__dados


class Disciplina(object):

    __dados = []

    def __init__(self, nome, curso, semestre, carga_presencial, carga_ead):
        self.nome = nome
        self.curso = curso
        self.semestre = semestre
        self.carga_presencial = carga_presencial
        self.carga_ead = carga_ead

    def __str__(self):
        return f'{self.nome}'

    @classmethod
    def criar(cls, nome, curso, semestre, carga_presencial, carga_ead):
        Disciplina.__dados.append(
            cls(nome, curso, semestre, carga_presencial, carga_ead)
        )

    @classmethod
    def filtrar(cls, curso_sigla):
        return [d
                for d in Disciplina.__dados
                if d.curso.sigla.lower() == curso_sigla.lower()
                ]

    @classmethod
    def listar(cls):
        return Disciplina.__dados


class Premio(object):

    __dados = []

    def __init__(self, titulo, descricao, curso):
        self.titulo = titulo
        self.descricao = descricao
        self.curso = curso

    def __str__(self):
        return f'{self.titulo}'

    @classmethod
    def criar(cls, titulo, descricao, curso):
        Premio.__dados.append(
            cls(titulo, descricao, curso)
        )

    @classmethod
    def listar(cls):
        return Premio.__dados

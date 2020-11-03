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
    def alterar(cls, nome, sigla, tipo, descricao, coordenador,
                duracao, diurno, noturno):
        curso = cls(nome, sigla, tipo, descricao, coordenador,
                    duracao, diurno, noturno)
        erros = Curso.__validar(curso, True)

        if len(erros) == 0:
            original = Curso.obter(curso.sigla)
            original.nome = curso.nome
            original.sigla = curso.sigla
            original.tipo = curso.tipo
            original.descricao = curso.descricao
            original.coordenador = curso.coordenador
            original.duracao = curso.duracao
            original.diurno = curso.diurno
            original.noturno = curso.noturno

        return erros

    @classmethod
    def criar(cls, nome, sigla, tipo, descricao, coordenador,
              duracao, diurno, noturno):
        curso = cls(nome, sigla, tipo, descricao, coordenador,
                    duracao, diurno, noturno)
        erros = Curso.__validar(curso)

        if len(erros) == 0:
            Curso.__dados.append(curso)

        return erros

    @classmethod
    def remover(cls, sigla):
        curso = Curso.obter(sigla)
        if curso:
            Curso.__dados.remove(curso)

    @classmethod
    def obter(cls, sigla):
        for c in Curso.__dados:
            if c.sigla.lower() == sigla.lower():
                return c

    @classmethod
    def listar(cls):
        return Curso.__dados

    @classmethod
    def __validar(cls, curso, alteracao=False):
        erros = []
        if not curso.nome:
            erros.append('Nome do curso é obrigatório!')

        if not curso.sigla:
            erros.append('Sigla do curso é obrigatória!')
        elif not alteracao and Curso.obter(curso.sigla):
            erros.append(f'A sigla {curso.sigla} já está sendo utilizada!')

        if not curso.tipo:
            erros.append('Tipo do curso é obrigatório!')

        return erros


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


class Usuario(object):

    __dados = []

    def __init__(self, usuario, nome, email, senha):
        self.usuario = usuario
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return self.nome

    @classmethod
    def autenticar(cls, usuario, senha):
        usuario = Usuario.obter(usuario)
        if usuario and usuario.senha == senha:
            return usuario

    @classmethod
    def criar(cls, usuario, nome, email, senha):
        Usuario.__dados.append(
            cls(usuario, nome, email, senha)
        )

    @classmethod
    def obter(cls, usuario):
        for u in Usuario.__dados:
            if u.usuario == usuario:
                return u

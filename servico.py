import sqlite3
from entidades import Usuario, Anotacao, Tarefa, Materia

class Servico:

    # BANCO DE DADOS

    def __init__(self, nome_do_banco):
        self.nome_do_banco = nome_do_banco
        self.conexao = sqlite3.connect(self.nome_do_banco)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conexao.cursor()


    def salvar(self):
        self.conexao.commit()
    
    def salvar_consulta(self):
        return self.cursor.fetchall()

    def salvar_consulta1(self):
        return self.cursor.fetchone()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()

    def proximo_codigo(self, tabela):
        self.cursor.execute(f"SELECT MAX(codigo) FROM {tabela}")
        resultado = self.cursor.fetchone()[0]
        if resultado is None:
            return 1   # se a tabela estiver vazia
        else:
            return resultado + 1

    # -- DDL --

    def criar_tabelas(self):
        self.cursor.executescript("""
CREATE TABLE IF NOT EXISTS usuario (
    email TEXT NOT NULL,
    nome  TEXT NOT NULL,
    senha TEXT NOT NULL,
    CONSTRAINT PKUsuario PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS materia (
    codigo INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricao TEXT,
    emailUsuario TEXT NOT NULL,
    CONSTRAINT PKMateria PRIMARY KEY(codigo),
    CONSTRAINT FK_Materia_Usuario FOREIGN KEY (emailUsuario) REFERENCES usuario(email)
);

CREATE TABLE IF NOT EXISTS anotacao (
    codigo INTEGER NOT NULL,
    dataCriacao TEXT DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT,
    emailUsuario TEXT NOT NULL,
    codigoMateria INTEGER NOT NULL,
    CONSTRAINT PKAnotacao PRIMARY KEY(codigo),
    CONSTRAINT FK_Anotacao_Usuario FOREIGN KEY (emailUsuario) REFERENCES usuario(email),
    CONSTRAINT FK_Anotacao_Materia FOREIGN KEY (codigoMateria) REFERENCES materia(codigo)
);

CREATE TABLE IF NOT EXISTS tarefa (
    codigo INTEGER NOT NULL,
    dataCriacao TEXT DEFAULT CURRENT_TIMESTAMP,
    dataFinalizacao TEXT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT NOT NULL, -- ex: 'A' ou 'F'
    emailUsuario TEXT NOT NULL,
    codigoMateria INTEGER NOT NULL,
    CONSTRAINT PKTarefa PRIMARY KEY(codigo),
    CONSTRAINT FK_Tarefa_Usuario FOREIGN KEY (emailUsuario) REFERENCES usuario(email),
    CONSTRAINT FK_Tarefa_Materia FOREIGN KEY (codigoMateria) REFERENCES materia(codigo)
);
""")
        self.salvar()

    # -- DML -- 

    def dados_teste(self):
        self.cursor.executescript("""
INSERT OR IGNORE INTO usuario (email, nome, senha) VALUES
('joao@email.com', 'João Silva', '123456'),
('maria@email.com', 'Maria Souza', '654321');

INSERT OR IGNORE INTO materia (codigo, titulo, descricao, emailUsuario) VALUES
(1, 'Algoritmos', 'Introdução à lógica de programação e estruturas de repetição.', 'joao@email.com'),
(2, 'Banco de Dados', 'Modelagem e SQL aplicado.', 'joao@email.com'),
(3, 'Engenharia de Software', 'Conceitos de análise e desenvolvimento.', 'joao@email.com'),
(4, 'Estruturas de Dados', 'Listas, pilhas, filas e árvores.', 'maria@email.com'),
(5, 'Programação em C', 'Linguagem C aplicada a problemas práticos.', 'maria@email.com');

INSERT OR IGNORE INTO anotacao (codigo, dataCriacao, descricao, emailUsuario, codigoMateria) VALUES
(1, CURRENT_TIMESTAMP, 'Resumo sobre estruturas de repetição.', 'joao@email.com', 1),
(2, CURRENT_TIMESTAMP, 'Exemplos de SELECT com JOIN.', 'joao@email.com', 2),
(3, CURRENT_TIMESTAMP, 'Modelo cascata vs ágil.', 'joao@email.com', 3),
(4, CURRENT_TIMESTAMP, 'Resumo de listas encadeadas.', 'maria@email.com', 4),
(5, CURRENT_TIMESTAMP, 'Comandos básicos em C.', 'maria@email.com', 5);

INSERT OR IGNORE INTO tarefa (codigo, dataCriacao, dataFinalizacao, titulo, descricao, status, emailUsuario, codigoMateria) VALUES
(1, CURRENT_TIMESTAMP, NULL, 'Lista de exercícios de Algoritmos', 'Fazer exercícios do capítulo 2.', 'A', 'joao@email.com', 1),
(2, CURRENT_TIMESTAMP, NULL, 'Trabalho Banco de Dados', 'Criar diagrama ER.', 'A', 'joao@email.com', 2),
(3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Resumo Engenharia de Software', 'Entregar resumo de metodologias.', 'F', 'joao@email.com', 3),
(4, CURRENT_TIMESTAMP, NULL, 'Implementar lista encadeada', 'Exercício prático em C.', 'A', 'maria@email.com', 4),
(5, CURRENT_TIMESTAMP, NULL, 'Estudar ponteiros', 'Revisar capítulo de ponteiros.', 'A', 'maria@email.com', 5),
(6, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Exercícios Banco de Dados', 'Queries de junção.', 'F', 'maria@email.com', 2),
(7, CURRENT_TIMESTAMP, NULL, 'Resumo Estruturas de Dados', 'Preparar para prova.', 'A', 'joao@email.com', 4),
(8, CURRENT_TIMESTAMP, NULL, 'Projeto final C', 'Desenvolver mini sistema em C.', 'A', 'maria@email.com', 5);
""")
        self.salvar()
    
    # USUARIO

    def usuario_criar(self, usuario):
        self.cursor.execute("INSERT INTO usuario(email, senha, nome) VALUES (?,?,?)",(usuario.email, usuario.senha, usuario.nome))
        self.salvar()

    def usuario_alterar(self, usuario):
        self.cursor.execute("UPDATE usuario SET senha = ?, nome = ? WHERE email=?",(usuario.senha,usuario.nome, usuario.email))
        self.salvar()
    
    def usuario_deletar(self, usuario):
        self.cursor.execute("DELETE FROM usuario WHERE email = ?", (usuario.email,))
        self.salvar()

    def usuarios_listar(self):
        self.cursor.execute("SELECT * FROM usuario")
        dados = self.salvar_consulta()
        return dados

    def usuario_1(self, email):
        self.cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
        dados = self.salvar_consulta1()
        if dados:
            usuario = Usuario(dados[0], dados[1], dados[2])
            return usuario
        else:
            return None

    def usuario_login(self, email, senha):
        self.cursor.execute("SELECT * FROM usuario WHERE email = ? AND senha = ?", (email, senha) )
        dados = self.salvar_consulta1()
        if dados:
            usuario = Usuario(dados[0], dados[1], dados[2])
            return usuario
        else:
            return None

    # MATERIA

    def materia_criar(self, materia):
        self.cursor.execute("INSERT INTO materia(codigo, titulo, descricao, emailUsuario) VALUES (?,?,?,?)",(materia.codigo, materia.titulo, materia.descricao, materia.emailUsuario))
        self.salvar()

    def materia_alterar(self, materia):
        self.cursor.execute("UPDATE materia SET titulo = ?, descricao = ?, emailUsuario = ? WHERE codigo = ?",(materia.titulo, materia.descricao, materia.emailUsuario, materia.codigo))
        self.salvar()
    
    def materia_deletar(self, materia):
        self.cursor.execute("DELETE FROM materia WHERE codigo = ?", (materia.codigo,))
        self.salvar()

    def materia_listar(self):
        self.cursor.execute("SELECT * FROM materia")
        dados = self.salvar_consulta()
        return dados
    
    def materia_1(self, codigo):
        self.cursor.execute("SELECT * FROM materia WHERE codigo = ?", (codigo,))
        dados = self.salvar_consulta1()
        return dados

    # TAREFA

    def tarefa_criar(self, tarefa):
        self.cursor.execute(
        "INSERT INTO tarefa(codigo, titulo, descricao, status, dataCriacao, emailUsuario, codigoMateria) "
        "VALUES (?,?,?, ?, CURRENT_TIMESTAMP, ?, ?)",
        (tarefa.codigo, tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.emailUsuario, tarefa.codigoMateria)
    )
        self.salvar()


    def tarefa_alterar(self, tarefa):
        self.cursor.execute("UPDATE tarefa SET titulo = ?, descricao = ?, status = ?, codigoMateria = ?, emailUsuario = ? WHERE codigo = ?",(tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.codigoMateria, tarefa.emailUsuario, tarefa.codigo))
        self.salvar()
    
    def tarefa_deletar(self, tarefa):
        self.cursor.execute("DELETE FROM tarefa WHERE codigo = ?", (tarefa.codigo,))
        self.salvar()

    def tarefa_listar(self):
        self.cursor.execute("SELECT * FROM tarefa")
        dados = self.salvar_consulta()
        return dados
    
    def tarefa_1(self, codigo):
        self.cursor.execute("SELECT * FROM tarefa WHERE codigo = ?", (codigo,))
        dados = self.salvar_consulta1()
        return dados

    # ANOTACAO

    def anotacao_criar(self, anotacao):
        self.cursor.execute(
        "INSERT INTO anotacao(codigo, dataCriacao, descricao, emailUsuario, codigoMateria) "
        "VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?)",
        (anotacao.codigo, anotacao.descricao, anotacao.emailUsuario, anotacao.codigoMateria)
    )
        self.salvar()

    def anotacao_alterar(self, anotacao):
        self.cursor.execute("UPDATE anotacao SET dataCriacao = ?, descricao = ?, codigoMateria = ?, emailUsuario = ? WHERE codigo = ?",(anotacao.dataCriacao, anotacao.descricao, anotacao.codigoMateria, anotacao.emailUsuario, anotacao.codigo))
        self.salvar()
    
    def anotacao_deletar(self, anotacao):
        self.cursor.execute("DELETE FROM anotacao WHERE codigo = ?", (anotacao.codigo,))
        self.salvar()

    def anotacao_listar(self):
        self.cursor.execute("SELECT * FROM anotacao")
        dados = self.salvar_consulta()
        return dados
    
    def anotacao_1(self, codigo):
        self.cursor.execute("SELECT * FROM anotacao WHERE codigo = ?", (codigo,))
        dados = self.salvar_consulta1()
        return dados

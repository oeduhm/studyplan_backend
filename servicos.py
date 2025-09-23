import sqlite3
from entidades import Usuario, Materia, Anotacao, Tarefa  

class Servico:

    # BANCO DE DADOS

    def __init__(self, nome_do_banco):
        self.nome_do_banco = nome_do_banco
        self.conexao = sqlite3.connect(self.nome_do_banco)
        self.cursor = self.conexao.cursor()

    def salvar(self):
        self.conexao.commit()
    
    def salvar_consulta(self):
        dados = self.cursor.fetchall()
        return dados

    def fechar(self):
        self.cursor.close()

    # -- DDL --

    # CRIACAO TABELAS ETC

    # -- DML -- 

    # USUARIO

    def usuario_c(self, usuario):
        self.cursor.execute("INSERT INTO usuario(email, senha, nome) VALUES (?,?,?)",(usuario.email, usuario.senha, usuario.nome))
        self.salvar()

    def usuario_a(self, usuario):
        self.cursor.execute("UPDATE usuario SET email = ?, senha = ?, nome = ?",(usuario.email,usuario.senha,usuario.nome))
        self.salvar()
    
    def usuario_d(self, usuario):
        self.cursor.execute("DELETE usuario WHERE email = ?", (usuario.email,))

    def usuarios_listar(self):
        self.cursor.execute("SELECT * FROM usuario")
        dados = self.salvar_consulta()
        return dados

    def usuario_1(self, codigo):
        self.cursor.execute("SELECT * FROM usuario WHERE id = ?", (codigo,))
        dados = self.salvar_consulta()
        return dados

    def usuario_login(self, usuario):
        self.cursor.execute("SELECT * FROM usuario WHERE email = ?, senha = ?", (usuario.email, usuario.senha) )
        dados = self.salvar_consulta()
        if dados:
            return usuario
        else:
            return None

    # MATERIA

    def materia_c(self, materia):
        self.cursor.execute("INSERT INTO materia(titulo, descricao, emailUsuario) VALUES (?,?,?)",(materia.titulo, materia.descricao, materia.emailUsuario))
        self.salvar()

    def materia_a(self, materia):
        self.cursor.execute("UPDATE materia SET titulo = ?, descricao = ?, emailUsuario = ?",(materia.titulo, materia.descricao, Materia.emailUsuario))
        self.salvar()
    
    def materia_d(self, materia):
        self.cursor.execute("DELETE materia WHERE codigo = ?", (materia.codigo,))
        self.salvar()

    def materia_listar(self):
        self.cursor.execute("SELECT * FROM materia")
        dados = self.salvar_consulta()
        return dados
    
    def materia_1(self, codigo):
        self.cursor.execute("SELECT * FROM materia WHERE codigo = ?", (codigo,))
        dados = self.salvar_consulta()
        return dados

    # TAREFA

    def tarefa_c(self, tarefa):
        self.cursor.execute("INSERT INTO tarefa(titulo, descricao, status, dataCriacao, codigoMateria, emailUsuario) VALUES (?,?,?,?,?,?)",(tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.codigoMateria, tarefa.emailUsuario))
        self.salvar()

    def tarefa_a(self, tarefa):
        self.cursor.execute("UPDATE tarefa SET titulo = ?, descricao = ?, status = ?, codigoMateria = ?, emailUsuario = ?",(tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.codigoMateria, tarefa.emailUsuario))
        self.salvar()
    
    def tarefa_d(self, tarefa):
        self.cursor.execute("DELETE tarefa WHERE codigo = ?", (tarefa.codigo,))
        self.salvar()

    def tarefa_listar(self):
        self.cursor.execute("SELECT * FROM tarefa")
        dados = self.salvar_consulta()
        return dados
    
    def tarefa_1(self, codigo):
        self.cursor.execute("SELECT * FROM tarefa WHERE codigo = ?", (codigo,))
        dados = self.salvar_consulta()
        return dados

    # ANOTACAO

    def anotacao_c(self, anotacao):
        self.cursor.execute("INSERT INTO anotacao(dataCriacao, descricao, codigoMateria, emailUsuario) VALUES (?,?,?,?,?,?)",(anotacao.dataCriacao, anotacao.descricao, anotacao.codigoMateria, anotacao.emailUsuario))
        self.salvar()

    def anotacao_a(self, anotacao):
        self.cursor.execute("UPDATE anotacao SET dataCriacao = ?, descricao = ?, codigoMateria = ?, emailUsuario = ?",(anotacao.dataCriacao, anotacao.descricao, anotacao.codigoMateria, anotacao.emailUsuario))
        self.salvar()
    
    def anotacao_d(self, anotacao):
        self.cursor.execute("DELETE anotacao WHERE codigo = ?", (anotacao.codigo,))
        self.salvar()

    def anotacao_listar(self):
        self.cursor.execute("SELECT * FROM anotacao")
        dados = self.salvar_consulta()
        return dados
    
    def anotacao_1(self, codigo):
        self.cursor.execute("SELECT * FROM anotacao WHERE codigo = ?", (codigo,))
        dados = self.salvar_consulta()
        return dados

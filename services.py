from entities import Usuario, Anotacao, Tarefa, Materia

class Servico:
    def __init__(self, bd):
        self.bd = bd

    def proximo_codigo(self, tabela):
        try:
            self.bd.cursor.execute(f"SELECT COALESCE(MAX(codigo), 0) FROM {tabela}")
            resultado = self.bd.cursor.fetchone()[0]
            return int(resultado) + 1
        except Exception:
            return 1

    # USUARIO
    def usuario_criar(self, usuario):
        self.bd.cursor.execute(
            "INSERT INTO usuario(email, senha, nome) VALUES (%s, %s, %s) ON CONFLICT (email) DO NOTHING",
            (usuario.email, usuario.senha, usuario.nome)
        )
        self.bd.salvar()

    def usuario_alterar(self, usuario):
        self.bd.cursor.execute(
            "UPDATE usuario SET senha = %s, nome = %s WHERE email = %s",
            (usuario.senha, usuario.nome, usuario.email)
        )
        self.bd.salvar()
    
    def usuario_deletar(self, usuario):
        self.bd.cursor.execute("DELETE FROM usuario WHERE email = %s", (usuario.email,))
        self.bd.salvar()

    def usuarios_listar(self):
        self.bd.cursor.execute("SELECT email, nome, senha FROM usuario")
        return self.bd.salvar_consulta()

    def usuario_1(self, email):
        self.bd.cursor.execute("SELECT email, nome, senha FROM usuario WHERE email = %s", (email,))
        dados = self.bd.salvar_consulta1()
        if dados:
            return Usuario(dados[0], dados[1], dados[2])
        return None

    def usuario_login(self, email, senha):
        self.bd.cursor.execute("SELECT email, nome, senha FROM usuario WHERE email = %s AND senha = %s", (email, senha))
        dados = self.bd.salvar_consulta1()
        if dados:
            return Usuario(dados[0], dados[1], dados[2])
        return None

    # MATERIA
    def materia_criar(self, materia):
        self.bd.cursor.execute(
            "INSERT INTO materia(codigo, titulo, descricao, emailUsuario) VALUES (%s, %s, %s, %s)",
            (materia.codigo, materia.titulo, materia.descricao, materia.emailUsuario)
        )
        self.bd.salvar()

    def materia_alterar(self, materia):
        self.bd.cursor.execute(
            "UPDATE materia SET titulo = %s, descricao = %s, emailUsuario = %s WHERE codigo = %s",
            (materia.titulo, materia.descricao, materia.emailUsuario, materia.codigo)
        )
        self.bd.salvar()
    
    def materia_deletar(self, materia):
        self.bd.cursor.execute("DELETE FROM materia WHERE codigo = %s AND emailUsuario = %s", (materia.codigo,materia.emailUsuario))
        self.bd.salvar()

    def materia_listar(self):
        self.bd.cursor.execute("SELECT codigo, titulo, descricao, emailUsuario FROM materia")
        return self.bd.salvar_consulta()
    
    def materia_1(self, codigo):
        self.bd.cursor.execute("SELECT codigo, titulo, descricao, emailUsuario FROM materia WHERE codigo = %s", (codigo,))
        dados = self.bd.salvar_consulta1()
        if dados:
            return Materia(dados[0], dados[1], dados[2], dados[3])
        return None

    # TAREFA
    def tarefa_criar(self, tarefa):
        self.bd.cursor.execute(
            """
            INSERT INTO tarefa(codigo, titulo, descricao, status, dataCriacao, emailUsuario, codigoMateria)
            VALUES (%s, %s, %s, %s, now(), %s, %s)
            """,
            (tarefa.codigo, tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.emailUsuario, tarefa.codigoMateria)
        )
        self.bd.salvar()

    def tarefa_alterar(self, tarefa):
        self.bd.cursor.execute(
            """
            UPDATE tarefa
               SET titulo = %s, descricao = %s, status = %s, codigoMateria = %s, emailUsuario = %s
             WHERE codigo = %s
            """,
            (tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.codigoMateria, tarefa.emailUsuario, tarefa.codigo)
        )
        self.bd.salvar()
    
    def tarefa_deletar(self, tarefa):
        self.bd.cursor.execute("DELETE FROM tarefa WHERE codigo = %s AND emailUsuario = %s", (tarefa.codigo,tarefa.emailUsuario))
        self.bd.salvar()

    def tarefa_listar(self):
        self.bd.cursor.execute("""
            SELECT codigo, dataCriacao, dataFinalizacao, titulo, descricao, status, emailUsuario, codigoMateria
            FROM tarefa
        """)
        return self.bd.salvar_consulta()
    
    def tarefa_1(self, codigo):
        self.bd.cursor.execute("""
            SELECT codigo, dataCriacao, dataFinalizacao, titulo, descricao, status, emailUsuario, codigoMateria
            FROM tarefa
            WHERE codigo = %s
        """, (codigo,))
        return self.bd.salvar_consulta1()

    # ANOTACAO
    def anotacao_criar(self, anotacao):
        if (anotacao.codigoMateria is not None and anotacao.codigoTarefa is not None) or \
           (anotacao.codigoMateria is None and anotacao.codigoTarefa is None):
            raise ValueError("A anotação deve estar vinculada a uma matéria OU a uma tarefa, nunca ambas ou nenhuma.")

        self.bd.cursor.execute(
            """
            INSERT INTO anotacao (codigo, dataCriacao, descricao, emailUsuario, codigoMateria, codigoTarefa)
            VALUES (%s, now(), %s, %s, %s, %s)
            """,
            (anotacao.codigo, anotacao.descricao, anotacao.emailUsuario, anotacao.codigoMateria, anotacao.codigoTarefa)
        )
        self.bd.salvar()

    def anotacao_alterar(self, anotacao):
        self.bd.cursor.execute(
            """
            UPDATE anotacao
               SET dataCriacao = now(), descricao = %s, codigoMateria = %s, codigoTarefa = %s, emailUsuario = %s
             WHERE codigo = %s
            """,
            (anotacao.descricao, anotacao.codigoMateria, anotacao.codigoTarefa, anotacao.emailUsuario, anotacao.codigo)
        )
        self.bd.salvar()
    
    def anotacao_deletar(self, anotacao):
        self.bd.cursor.execute("DELETE FROM anotacao WHERE codigo = %s AND emailUsuario = %s", (anotacao.codigo, anotacao.emailUsuario))
        self.bd.salvar()

    def anotacao_listar(self):
        self.bd.cursor.execute("""
            SELECT codigo, dataCriacao, descricao, emailUsuario, codigoMateria, codigoTarefa
            FROM anotacao
        """)
        return self.bd.salvar_consulta()
    
    def anotacao_1(self, codigo):
        self.bd.cursor.execute("""
            SELECT codigo, dataCriacao, descricao, emailUsuario, codigoMateria, codigoTarefa
            FROM anotacao
            WHERE codigo = %s
        """, (codigo,))
        return self.bd.salvar_consulta1()



from entidades import Usuario, Anotacao, Tarefa, Materia
from servico import Servico

s = Servico("banco.db")
s.criar_tabelas()
s.dados_teste()

lista_usuarios = s.usuarios_listar()
lista_materias = s.materia_listar()
lista_tarefas = s.tarefa_listar()
lista_anotacoes = s.anotacao_listar()

print("Usuários:")
for email, senha, nome in lista_usuarios:
    print(nome, email, senha)

print("Matérias:")
for codigo, titulo, descricao, emailUsuario in lista_materias:
    print(codigo, titulo, descricao, emailUsuario)

print("Tarefas:")
for codigo, dataCriacao, dataFinalizacao, titulo, descricao, status, emailUsuario, codigoMateria in lista_tarefas:
    print(codigo, dataCriacao, dataFinalizacao, titulo, descricao, status, emailUsuario, codigoMateria)

print("Anotações:")
for codigo, dataCriacao, descricao, emailUsuario, codigoMateria in lista_anotacoes:
    print(codigo, dataCriacao, descricao, emailUsuario, codigoMateria)

# Testar cada método...

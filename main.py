from entidades import Usuario, Anotacao, Tarefa, Materia
from servico import Servico

s = Servico("banco.db")
s.criar_tabelas()
s.dados_teste()

# Teste Métodos

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
for codigo, dataCriacao, descricao, emailUsuario, codigoMateria, codigoTarefa in lista_anotacoes:
    print(codigo, dataCriacao, descricao, emailUsuario, codigoMateria, codigoTarefa)

print("Login:")
usuario = s.usuario_login("joao@email.com","123456")
if usuario:
    print(usuario.email, usuario.senha, usuario.nome)
else:
    print("Nada encontrado no banco de dados.")

usuario_alterado = Usuario("joao@email.com.br", "1234567", "Senhor João")

print("Alterar Usuário:")
s.usuario_alterar(usuario_alterado)
print(usuario_alterado.nome)

print("Criar Usuário:")
novo_usuario = Usuario("novo@novo.com.br", "123", "Novo")
#s.usuario_criar(novo_usuario)
a1 = s.usuario_1("novo@novo.com.br")

print("Deletar Usuário:")
#s.usuario_deletar(novo_usuario)
print(s.usuarios_listar())

print("Busca por Usuario no Banco:")
b1 = s.usuario_1("joao@email.com")
if b1:
    print(b1.nome)
else:
    print("Nada encontrado.")

print(s.usuarios_listar())

print("Matéria")
nova_materia = Materia(s.proximo_codigo("materia"),"Materia Teste", "Descrição da Matéria teste", "joao@email.com")
#s.materia_criar(nova_materia)

materia_alterada = Materia(6, "Materia Teste Alterada", "Nova descrição.", "joao@email.com")
s.materia_alterar(materia_alterada)

print(s.materia_1(3).titulo)

#s.materia_deletar(s.materia_1(7))

tarefa1 = Tarefa(s.proximo_codigo("tarefa"), "Nome da Tarefa", "Desc", "A", None, None , 6 ,"joao@email.com")
# s.tarefa_criar(tarefa1)

tarefa1_alterada = Tarefa(9, "Nome da Tarefa Alterado", "Descricao alterada", "A", None, None, 6, "joao@email.com")
s.tarefa_alterar(tarefa1_alterada)

# s.tarefa_deletar(tarefa1_alterada)
print(s.tarefa_1(10))

anotacao1 = Anotacao(s.proximo_codigo("anotacao"), None, "Descrição da anotação.", "joao@email.com", 5, None)
s.anotacao_criar(anotacao1)

s.anotacao_alterar(Anotacao(7,None, "desc alterada", "joao@email.com", 1, None))

# s.anotacao_deletar(anotacao1)


s.fechar()


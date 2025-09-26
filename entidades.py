# ENTIDADES

class Usuario:
    def __init__(self, email, senha, nome):
        self.__email = email
        self.__senha = senha
        self.__nome = nome

    @property 
    def email(self):
        return self.__email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property 
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        self.__senha = valor


class Materia:
    def __init__(self, codigo, titulo, descricao, emailUsuario):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__descricao = descricao
        self.__emailUsuario = emailUsuario
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,valor):
        self.__codigo = valor

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor
    
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def emailUsuario(self):
        return self.__emailUsuario

    @emailUsuario.setter
    def emailUsuario(self, valor):
        self.__emailUsuario = valor

class Anotacao:
    def __init__(self, codigo, dataCriacao, descricao, emailUsuario, codigoMateria, codigoTarefa):
        self.__codigo = codigo
        self.__dataCriacao = dataCriacao
        self.__descricao = descricao
        self.__emailUsuario = emailUsuario
        self.__codigoMateria = codigoMateria
        self.__codigoTarefa = codigoTarefa

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def dataCriacao(self):
        return self.__dataCriacao

    @dataCriacao.setter
    def dataCriacao(self, valor):
        self.__dataCriacao = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor
    
    @property
    def emailUsuario(self):
        return self.__emailUsuario

    @emailUsuario.setter
    def emailUsuario(self, valor):
        self.__emailUsuario = valor

    @property
    def codigoMateria(self):
        return self.__codigoMateria

    @codigoMateria.setter
    def codigoMateria(self, valor):
        self.__codigoMateria = valor

    @property
    def codigoTarefa(self):
        return self.__codigoTarefa
    
    @codigoTarefa.setter
    def codigoTarefa(self, valor):
        self.__codigoTarefa = valor

class Tarefa:
    def __init__(self, codigo, titulo, descricao, status, dataCriacao, dataFinalizacao, codigoMateria, emailUsuario):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__descricao = descricao
        self.__status = status
        self.__dataCriacao = dataCriacao
        self.__dataFinalizacao = dataFinalizacao 
        self.__codigoMateria = codigoMateria
        self.__emailUsuario = emailUsuario

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property 
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor

    @property
    def dataCriacao(self):
        return self.__dataCriacao

    @dataCriacao.setter
    def dataCriacao(self, valor):
        self.__dataCriacao = valor

    @property
    def dataFinalizacao(self):
        return self.__dataFinalizacao

    @dataFinalizacao.setter
    def dataFinalizacao(self, valor):
        self.__dataFinalizacao = valor    

    @property
    def codigoMateria(self):
        return self.__codigoMateria

    @codigoMateria.setter
    def codigoMateria(self, valor):
        self.__codigoMateria = valor
    
    @property
    def emailUsuario(self):
        return self.__emailUsuario
    
    @emailUsuario.setter
    def emailUsuario(self, valor):
        self.__emailUsuario = valor



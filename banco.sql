CREATE TABLE usuario (
    email varchar(20) NOT NULL,
    nome varchar(20) NOT NULL,
    senha varchar(6) NOT NULL,
    CONSTRAINT PKUsuario PRIMARY KEY (email)
);

CREATE TABLE materia (
    codigo integer NOT NULL,
    titulo varchar(60) NOT NULL,
    descricao varchar(500),
    emailUsuario varchar(20) NOT NULL,
    CONSTRAINT PKMateria PRIMARY KEY(codigo),
    CONSTRAINT FK_Materia_Usuario FOREIGN KEY (emailUsuario) REFERENCES usuario(email)
);

CREATE TABLE anotacao (
    codigo integer NOT NULL,
    dataCriacao timestamp,
    descricao varchar(350),
    emailUsuario varchar(20) NOT NULL,
    codigoMateria integer NOT NULL,
    CONSTRAINT PKAnotacao PRIMARY KEY(codigo),
    CONSTRAINT FK_Anotacao_Usuario FOREIGN KEY (emailUsuario) REFERENCES usuario(email),
    CONSTRAINT FK_Anotacao_Materia FOREIGN KEY (codigoMateria) REFERENCES materia(codigo)
);

CREATE TABLE tarefa (
    codigo integer NOT NULL,
    dataCriacao timestamp,
    dataFinalizacao timestamp,
    titulo varchar(60) NOT NULL,
    descricao varchar(350),
    status char(1) NOT NULL,
    emailUsuario varchar(20) NOT NULL,
    codigoMateria integer NOT NULL,
    CONSTRAINT PKTarefa PRIMARY KEY(codigo),
    CONSTRAINT FK_Tarefa_Usuario FOREIGN KEY (emailUsuario) REFERENCES usuario(email),
    CONSTRAINT FK_Tarefa_Materia FOREIGN KEY (codigoMateria) REFERENCES materia(codigo)
);

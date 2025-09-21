INSERT INTO usuario (email, nome, senha) VALUES
('joao@email.com', 'João Silva', '123456'),
('maria@email.com', 'Maria Souza', '654321');

INSERT INTO materia (codigo, titulo, descricao, emailUsuario) VALUES
(1, 'Algoritmos', 'Introdução à lógica de programação e estruturas de repetição.', 'joao@email.com'),
(2, 'Banco de Dados', 'Modelagem e SQL aplicado.', 'joao@email.com'),
(3, 'Engenharia de Software', 'Conceitos de análise e desenvolvimento.', 'joao@email.com'),
(4, 'Estruturas de Dados', 'Listas, pilhas, filas e árvores.', 'maria@email.com'),
(5, 'Programação em C', 'Linguagem C aplicada a problemas práticos.', 'maria@email.com');

INSERT INTO anotacao (codigo, dataCriacao, descricao, emailUsuario, codigoMateria) VALUES
(1, NOW(), 'Resumo sobre estruturas de repetição.', 'joao@email.com', 1),
(2, NOW(), 'Exemplos de SELECT com JOIN.', 'joao@email.com', 2),
(3, NOW(), 'Modelo cascata vs ágil.', 'joao@email.com', 3),
(4, NOW(), 'Resumo de listas encadeadas.', 'maria@email.com', 4),
(5, NOW(), 'Comandos básicos em C.', 'maria@email.com', 5);

INSERT INTO tarefa (codigo, dataCriacao, dataFinalizacao, titulo, descricao, status, emailUsuario, codigoMateria) VALUES
(1, NOW(), NULL, 'Lista de exercícios de Algoritmos', 'Fazer exercícios do capítulo 2.', 'A', 'joao@email.com', 1),
(2, NOW(), NULL, 'Trabalho Banco de Dados', 'Criar diagrama ER.', 'A', 'joao@email.com', 2),
(3, NOW(), NOW(), 'Resumo Engenharia de Software', 'Entregar resumo de metodologias.', 'F', 'joao@email.com', 3),
(4, NOW(), NULL, 'Implementar lista encadeada', 'Exercício prático em C.', 'A', 'maria@email.com', 4),
(5, NOW(), NULL, 'Estudar ponteiros', 'Revisar capítulo de ponteiros.', 'A', 'maria@email.com', 5),
(6, NOW(), NOW(), 'Exercícios Banco de Dados', 'Queries de junção.', 'F', 'maria@email.com', 2),
(7, NOW(), NULL, 'Resumo Estruturas de Dados', 'Preparar para prova.', 'A', 'joao@email.com', 4),
(8, NOW(), NULL, 'Projeto final C', 'Desenvolver mini sistema em C.', 'A', 'maria@email.com', 5);

# BancoDeDados_Livros
 Projeto em Python que armazena livros num banco de dados (sqlite3) com Tkinter

 Este projeto foi feito para fixar os conhecimentos em Tkinter. 
 Ele é um aplicativo, feito em Tkinter, que armazena informações de livros em um banco de dados,
feito com o sqlite3.
 No aplicativo há função de adicionar novos livros e de deletar, alterar e buscar os já existentes
no banco.
 Além disso, o aplicativo mostrar informações como total de livros lidos, abandonados e afins em uma outra
aba.

 Para armazenar os livros temos alguns campos para serem preenchidos: nome do livro e posse do livro
(obrigatórios), nome do autor e nota do livro. Os campos de posse de livro e de nota contam com validadores
nas entrys para permitir apenas dados válidos (Sim ou Não no campo da posse; 0 a 10, Abandonado, --- ou vazio
no campo das notas).

 Também podemos organizar os livros na lista pela ordem alfabética dos nomes dos livros, pela ordem crescente ou
decrescente das notas dos livros.

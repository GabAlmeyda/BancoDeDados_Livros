from tkinter import *
from tkinter import messagebox
import sqlite3


class Functions:

    def __init__(self) -> None:
        self.__tipo_ordenacao = "nome_livro ASC"
        self.__tot_livros = 0
        self.__tot_livros_lidos = 0
        self.__tot_livros_abandonados = 0
        self.__tot_livros_possuidos = 0

    def get_tipo(self) -> str:
        return self.__tipo_ordenacao

    def set_tipo_nome(self) -> None:
        self.__tipo_ordenacao = "nome_livro ASC"
        self.select_lista()

    def set_tipo_autorASC(self) -> None:
        self.__tipo_ordenacao = "nome_autor ASC"
        self.select_lista()

    def set_tipo_notaDESC(self) -> None:
        self.__tipo_ordenacao = "nota DESC"
        self.select_lista()

    def __colocar_codigo(self, codigo) -> None:
        self.lb_codigo_dados = Label(self.aba1, text=codigo, bg="#404040", fg="light gray",
                                     font=("verdana", 10, "bold"))
        self.lb_codigo_dados.place(relx=0.07, rely=0.17, relwidth=0.03, relheight=0.06)

    def __retirar_codigo(self) -> None:
        try:
            self.lb_codigo_dados.destroy()
        except:
            pass

    def variaveis(self) -> None:
        if self.entry_nome.estado:
            self.livro = ""
        else:
            self.livro = self.entry_nome.get()

        if self.entry_autor.estado:
            self.autor = ""
        else:
            self.autor = str(self.entry_autor.get()).capitalize()

        if self.entry_nota.estado:
            self.nota = ""
        else:
            self.nota = str(self.entry_nota.get()).capitalize()

        if self.entry_posse.estado:
            self.posse = ""
        else:
            self.posse = str(self.entry_posse.get()).capitalize()

    def focar(self) -> None:
        self.entry_nome.foc_in()
        self.entry_autor.foc_in()
        self.entry_nota.foc_in()
        self.entry_posse.foc_in()

    def ao_passar(self, event) -> None:
        event.widget.config(bg="#640bdb")

    def ao_sair(self, event) -> None:
        event.widget.config(bg="#4a07a3")

    def __colocar_placeholder(self) -> None:
        self.frame_1.focus_set()
        for n in (self.entry_nome, self.entry_autor, self.entry_nota, self.entry_posse):
            n.put_placeholder()

    def limpar_tela(self) -> None:
        self.__retirar_codigo()
        self.entry_nome.delete(0, "end")
        self.entry_autor.delete(0, "end")
        self.entry_nota.delete(0, "end")
        self.entry_posse.delete(0, "end")
        self.__colocar_placeholder()

    def __conectar_bd(self) -> None:
        self.conn = sqlite3.connect("Livros.bd")
        self.cursor = self.conn.cursor()
        print('Conectando no Banco de Dados...')

    def __desconectar_bd(self) -> None:
        self.conn.close()
        print("Desconectando do Banco de Dados...")

    def montar_tabela(self) -> None:
        self.__conectar_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Livros(
                    cod INTEGER PRIMARY KEY,
                    nome_livro CHAR(40) NOT NULL,
                    nome_autor CHAR(30),
                    nota REAL(5),
                    possui CHAR(5)
                );
            """)
        self.conn.commit()
        print("Banco de Dados criado")
        self.__desconectar_bd()

    def __select_ordenado(self):
        lst = self.cursor.execute(f"""
                            SELECT cod, nome_livro, nome_autor, nota, possui FROM Livros
                            ORDER BY {self.__tipo_ordenacao};
                        """)
        return lst

    def select_lista(self) -> None:
        self.lista_livros.delete(*self.lista_livros.get_children())
        self.__conectar_bd()
        lista = self.__select_ordenado()
        for i in lista:
            self.lista_livros.insert("", END, values=i)
        self.__desconectar_bd()

    def __valida_add(self) -> bool:
        self.variaveis()
        validacao = False
        nome_janela = "Cadastro de Livros - Erro!"
        if self.livro == "":
            nome_erro = "Nome do livro necessário para adicioná-lo!"
            messagebox.showerror(nome_janela, nome_erro)
            self.entry_nome.focus_set()
        elif self.posse == "":
            posse_erro_vazio = "Posse do livro necessário para adicioná-lo!"
            messagebox.showerror(nome_janela, posse_erro_vazio)
            self.entry_posse.focus_set()
        elif self.posse != "Sim" and self.posse != "Não":
            posse_erro_errata = "O campo 'Posse' deve ser preenchido com 'Sim' ou 'Não'!"
            messagebox.showerror(nome_janela, posse_erro_errata)
            self.entry_posse.focus_set()
        else:
            validacao = True
        return validacao

    def add_livro(self) -> None:
        if self.__valida_add():
            self.__conectar_bd()
            self.cursor.execute("""
                    INSERT INTO Livros(nome_livro, nome_autor, nota, possui)
                    VALUES(?, ?, ?, ?)""", (self.livro, self.autor, self.nota, self.posse))
            self.conn.commit()
            self.__desconectar_bd()
            self.select_lista()
            self.limpar_tela()
            self.__tot_livros += 1
            self.widget_aba2()

    def duplo_clique(self, event) -> None:
        self.limpar_tela()

        for n in self.lista_livros.selection():
            col1, col2, col3, col4, col5 = self.lista_livros.item(n, "values")
            self.focar()
            global codigo
            codigo = col1
            self.__colocar_codigo(codigo)
            self.entry_nome.insert(END, col2)
            if col3 == "":
                self.entry_autor.put_placeholder()
            else:
                self.entry_autor.insert(END, col3)
            if col4 == "":
                self.entry_nota.put_placeholder()
            else:
                self.entry_nota.insert(END, col4)
            self.entry_posse.insert(END, col5)

    def deletar_livro(self) -> None:
        global codigo
        self.variaveis()
        self.__conectar_bd()
        self.cursor.execute("""
                DELETE FROM Livros WHERE cod = ?""", [codigo])
        self.conn.commit()
        self.__desconectar_bd()
        self.select_lista()
        self.limpar_tela()
        self.__tot_livros -= 1
        self.widget_aba2()

    def alterar_livro(self) -> None:
        global codigo
        self.variaveis()
        self.__conectar_bd()
        self.cursor.execute("""
                UPDATE Livros SET nome_livro = ?, nome_autor = ?, nota = ?, possui = ?
                WHERE cod = ?""", (self.livro, self.autor, self.nota, self.posse, codigo))
        self.conn.commit()
        self.__desconectar_bd()
        self.select_lista()
        self.limpar_tela()

    def __busca_ordenada(self, busca: str = "nome_livro", parametro: str = "") -> None:
        self.cursor.execute(f"""
                            SELECT cod, nome_livro, nome_autor, nota, possui FROM Livros
                            WHERE {busca} LIKE "%s" ORDER BY {self.__tipo_ordenacao}
                        """ % parametro)

    def buscar_livro(self, busca: str = "nome_livro") -> None:
        self.__conectar_bd()
        self.lista_livros.delete(*self.lista_livros.get_children())
        self.entry_nome.insert(END, '%')
        if busca == "nome_livro":
            if self.entry_nome.estado:
                parametro = "%"
            else:
                parametro = self.entry_nome.get()
        else:
            if self.entry_nota.estado:
                parametro = "%"
            else:
                parametro = self.entry_nota.get()
        self.__busca_ordenada(busca=busca, parametro=parametro)
        busca_nome_livro = self.cursor.fetchall()
        for i in busca_nome_livro:
            self.lista_livros.insert("", END, values=i)
        self.limpar_tela()
        self.__desconectar_bd()

    def selecionar_opcao(self, event) -> None:
        opcao = self.ddb_adicionais.get()
        if opcao == "Mostrar livros não lidos":
            self.entry_nota.foc_in()
            self.entry_nota.insert(END, "")
            self.buscar_livro("nota")
        elif opcao == "Mostrar livros abandonados":
            self.entry_nota.foc_in()
            self.entry_nota.insert(END, "Abandonado")
            self.buscar_livro("nota")
        elif opcao == "Mostrar todos os livros":
            self.entry_nome.foc_in()
            self.entry_nome.insert(END, "")
            self.buscar_livro()

    def total_livros(self) -> int:
        self.__tot_livros = 0
        self.__conectar_bd()
        lista = self.__select_ordenado()
        for i in lista:
            self.__tot_livros += 1
        self.__desconectar_bd()
        return self.__tot_livros

    def total_livros_lidos(self) -> int:
        self.__tot_livros_lidos = 0
        self.__conectar_bd()
        self.cursor.execute("""
                        SELECT COUNT(nota) FROM Livros WHERE nota NOT IN ("", "Abandonado") AND 
                        CAST(nota AS REAL) IS NOT NULL
                    """)
        self.__tot_livros_lidos = self.cursor.fetchone()[0]
        self.__desconectar_bd()
        return self.__tot_livros_lidos

    def total_livros_abandonados(self) -> int:
        self.__tot_livros_abandonados = 0
        self.__conectar_bd()
        self.cursor.execute("""
                    SELECT COUNT(nota) FROM Livros WHERE nota LIKE 'Abandonado'
                """)
        self.__tot_livros_abandonados = self.cursor.fetchone()[0]
        self.__desconectar_bd()
        return self.__tot_livros_abandonados

    def total_livros_possuidos(self) -> int:
        self.__tot_livros_possuidos = 0
        self.__conectar_bd()
        self.cursor.execute("""
                        SELECT COUNT(possui) FROM Livros WHERE possui LIKE "Sim"
                  """)
        self.__tot_livros_possuidos = self.cursor.fetchone()[0]
        self.__desconectar_bd()
        return self.__tot_livros_possuidos

from .functions import Functions
from .validators import Validators
from .placeholder import EntPlaceHolder
from tkinter import *
from tkinter import ttk


class Application(Functions, Validators):

    def __init__(self) -> None:
        super().__init__()
        self.janela = Tk()
        self.validaEntrada()
        self.tela()
        self.frames_tela()
        self.widget_frame_1()
        self.lista_frame_2()
        self.montar_tabela()
        self.select_lista()
        self.menus()
        self.widget_aba2()

        self.janela.focus_force()
        self.janela.mainloop()

    def centralizar_tela(self) -> None:
        tela_larg = self.janela.winfo_screenwidth()
        tela_alt = self.janela.winfo_screenheight()

        x = (tela_larg - 800) // 2
        y = (tela_alt - 600) // 2

        self.janela.geometry(f"800x600+{x}+{y}")

    def tela(self) -> None:
        self.janela.title("Avaliação de Livros")
        self.janela.configure(bg="#1c1b1b")
        self.centralizar_tela()
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=500)
        self.janela.maxsize(width=900, height=700)

    def frames_tela(self) -> None:
        self.frame_1 = Frame(self.janela, bd=2, bg="#303030", highlightbackground="#a202f0", highlightthickness=3)
        self.frame_1.place(relx=0.005, rely=0.009, relwidth=0.989, relheight=0.48)

        self.frame_2 = Frame(self.janela, bd=2, bg='#303030', highlightbackground="#A020F0", highlightthickness=3, )
        self.frame_2.place(relx=0.005, rely=0.52, relwidth=0.989, relheight=0.47)

    def __criar_abas(self) -> None:
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba1.configure(bg="#303030")
        self.aba2.configure(bg="#303030")
        self.abas.add(self.aba1, text="Gerenciar")
        self.abas.add(self.aba2, text="Adicionais")
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

    def __frame_1_LabelEntry(self) -> None:
        self.__criar_abas()

        self.lb_codigo = Label(self.aba1, text="Código", bg="#303030", fg="#A020F0",
                               font=("verdana", 10, "bold"))
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.07, relheight=0.1)

        self.canvas_codigo = Canvas(self.aba1, bg="#404040", bd=0, highlightthickness=2, highlightbackground="#a202f0")
        self.canvas_codigo.place(relx=0.05, rely=0.15, relwidth=0.07, relheight=0.1)

        self.lb_nome = Label(self.aba1, text="Nome do Livro", bg="#303030", fg="#A020F0",
                             font=("verdana", 10, "bold"))
        self.lb_nome.place(relx=0.05, rely=0.27, relwidth=0.14, relheight=0.1)
        self.entry_nome = EntPlaceHolder(self.aba1,  bg="#404040", fg="light gray", font=("verdana", 8, "bold"),
                                         placeholder="Digite o nome do livro")
        self.entry_nome.place(relx=0.05, rely=0.37, relwidth=0.5, relheight=0.1)

        self.lb_autor = Label(self.aba1, text="Nome do Autor", bg="#303030", fg="#A020F0",
                              font=("verdana", 10, "bold"))
        self.lb_autor.place(relx=0.05, rely=0.49, relwidth=0.14, relheight=0.1)
        self.entry_autor = EntPlaceHolder(self.aba1, bg="#404040", fg='light gray', font=("verdana", 8, "bold"),
                                          placeholder="Digite o nome do autor(a)")
        self.entry_autor.place(relx=0.05, rely=0.59, relwidth=0.5, relheight=0.107)

        self.lb_nota = Label(self.aba1, text="Nota (0-10)", bg="#303030", fg="#A202F0", font=("verdana", 10, "bold"))
        self.lb_nota.place(relx=0.05, rely=0.71, relwidth=0.12, relheight=0.1)
        self.entry_nota = EntPlaceHolder(self.aba1, bg="#404040", fg='light gray', font=("verdana", 8, "bold"), validate="key",
                                validatecommand=self.valida_nota, placeholder="Digite a nota")
        self.entry_nota.place(relx=0.05, rely=0.81, relwidth=0.13, relheight=0.1)

        self.lb_posse = Label(self.aba1, text="Está com o Livro?", bg='#303030', fg="#A202F0",
                              font=("verdana", 10, "bold"))
        self.lb_posse.place(relx=0.23, rely=0.71, relwidth=0.17, relheight=0.1)
        self.entry_posse = EntPlaceHolder(self.aba1, bg="#404040", fg="light gray", font=("verdana", 8, "bold"),
                                          validate="key", validatecommand=self.valida_posse, placeholder="Sim/Não")
        self.entry_posse.place(relx=0.23, rely=0.81, relwidth=0.19, relheight=0.1)

    def __frame_1_button(self) -> None:
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=2, bg="#4a07a3", fg="white",
                                activeforeground="white", activebackground="#640bdb",
                                font=("verdana", 10, "bold"), command=self.limpar_tela)
        self.bt_limpar.place(relx=0.35, rely=0.05, relwidth=0.1, relheight=0.15)
        self.bt_limpar.bind("<Enter>", self.ao_passar)
        self.bt_limpar.bind("<Leave>", self.ao_sair)

        self.bt_buscar = Button(self.aba1, text="Buscar", bd=2, bg="#4a07a3", fg="white",
                                activeforeground="white", activebackground="#640bdb",
                                font=("verdana", 10, "bold"), command=self.buscar_livro)
        self.bt_buscar.place(relx=0.45, rely=0.05, relwidth=0.1, relheight=0.15)
        self.bt_buscar.bind("<Enter>", self.ao_passar)
        self.bt_buscar.bind("<Leave>", self.ao_sair)

        self.bt_novo = Button(self.aba1, text="Novo", bd=2, bg="#4a07a3", fg="white",
                              activeforeground="white", activebackground="#640bdb",
                              font=("verdana", 10, "bold"), command=self.add_livro)
        self.bt_novo.place(relx=0.6, rely=0.05, relwidth=0.1, relheight=0.15)
        self.bt_novo.bind("<Enter>", self.ao_passar)
        self.bt_novo.bind("<Leave>", self.ao_sair)

        self.bt_alterar = Button(self.aba1, text="Alterar", fg="white", bd=2, bg="#4a07a3",
                                 activeforeground="white", activebackground="#640bdb",
                                 font=("verdana", 10, "bold"), command=self.alterar_livro)
        self.bt_alterar.place(relx=0.7, rely=0.05, relwidth=0.1, relheight=0.15)
        self.bt_alterar.bind("<Enter>", self.ao_passar)
        self.bt_alterar.bind("<Leave>", self.ao_sair)

        self.bt_apagar = Button(self.aba1, text="Apagar", fg="white", bd=2, bg="#4a07a3",
                                activeforeground="white", activebackground="#640bdb",
                                font=("verdana", 10, "bold"), command=self.deletar_livro)
        self.bt_apagar.place(relx=0.8, rely=0.05, relwidth=0.1, relheight=0.15)
        self.bt_apagar.bind("<Enter>", self.ao_passar)
        self.bt_apagar.bind("<Leave>", self.ao_sair)

    def widget_frame_1(self) -> None:
        self.__frame_1_LabelEntry()
        self.__frame_1_button()

    def lista_frame_2(self) -> None:
        style = ttk.Style(self.janela)
        style.theme_use("default")
        style.configure("Treeview", background="#8c8d8f", font=("verdana", 8, "bold", "italic"))
        self.lista_livros = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4", "col5"),
                                         style="Treeview")
        self.lista_livros.heading("#0", text="")
        self.lista_livros.heading("#1", text="Código")
        self.lista_livros.heading("#2", text="Nome do Livro")
        self.lista_livros.heading("#3", text="Autor(a)")
        self.lista_livros.heading("#4", text="Nota")
        self.lista_livros.heading("#5", text="Posse do Livro")
        self.lista_livros.column("#0", width=1)
        self.lista_livros.column("#1", width=50)
        self.lista_livros.column("#2", width=175)
        self.lista_livros.column("#3", width=175)
        self.lista_livros.column("#4", width=75)
        self.lista_livros.column("#5", width=75)
        self.lista_livros.place(relx=0.004, rely=0.01, relwidth=0.993, relheight=0.97)

        self.lista_livros.bind("<Double-1>", self.duplo_clique)

    def __aba2_LabelEntryDropDown(self) -> None:
        self.lb_adicionais = Label(self.aba2, text="Mostrar Livros Específicos:", bg="#303030", fg="#a202f0",
                                   font=("verdana", 10, "bold"))
        self.lb_adicionais.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.1)

        self.ddb_adicionais = StringVar()
        self.ddb_adicionais_lst = ("Mostrar livros não lidos", "Mostrar livros abandonados", "Mostrar todos os livros")
        self.ddb_adicionais.set("Clique Para Abrir")
        self.popup_menu = OptionMenu(self.aba2, self.ddb_adicionais, *self.ddb_adicionais_lst, command=self.selecionar_opcao)
        self.popup_menu.configure(bg="#640bdb", highlightthickness=1, highlightbackground="#a202f0",
                                  font=("verdana", 8, "bold"))
        self.popup_menu.place(relx=0.05, rely=0.15, relwidth=0.28, relheight=0.1)
        self.popup_menu.bind("<Enter>", self.ao_passar)
        self.popup_menu.bind("<Leave>", self.ao_sair)

        self.lb_info = Label(self.aba2, text=" Informações: ", bg="#303030", fg="#a202f0", font=("verdana", 11, "bold"))
        self.lb_info.place(relx=0.7, rely=0.05, relwidth=0.15, relheight=0.1)

        self.lb_total = Label(self.aba2, text="* Livros Cadastrados: ", bg="#303030", fg="#a202f0",
                              font=("verdana", 10, "bold", "italic"))
        self.lb_total.place(relx=0.72, rely=0.2, relwidth=0.233, relheight=0.1)

        def lb_total_resp():
            self.lb_total_resp = Label(self.aba2, text=self.total_livros(), bg="#303030", fg="#f002e8",
                                       font=("verdana", 10, "bold", "italic"))
            self.lb_total_resp.place(relx=0.96, rely=0.2, relwidth=0.035, relheight=0.1)
        lb_total_resp()

        self.lb_lidos = Label(self.aba2, text="* Livros Lidos: ", bg="#303030", fg="#a202f0",
                              font=("verdana", 10, "bold", "italic"))
        self.lb_lidos.place(relx=0.72, rely=0.3, relwidth=0.163, relheight=0.1)

        def lb_lidos_resp():
            self.lb_total_lidos = Label(self.aba2, text=self.total_livros_lidos(), bg="#303030", fg="#f002e8",
                                        font=("verdana", 10, "bold", "italic"))
            self.lb_total_lidos.place(relx=0.96, rely=0.3, relwidth=0.035, relheigh=0.1)
        lb_lidos_resp()

        self.lb_abandonados = Label(self.aba2, text="* Livros Abandonados: ", bg="#303030", fg="#a202f0",
                                    font=("verdana", 10, "bold", "italic"))
        self.lb_abandonados.place(relx=0.72, rely=0.4, relwidth=0.241, relheight=0.1)

        def lb_abandonados_resp():
            self.lb_abandonados_resp = Label(self.aba2, text=self.total_livros_abandonados(), bg="#303030", fg="#f002e8",
                                             font=("verdana", 10, "bold", "italic"))
            self.lb_abandonados_resp.place(relx=0.96, rely=0.4, relwidth=0.035, relheight=0.1)
        lb_abandonados_resp()

        self.lb_em_posse = Label(self.aba2, text="* Livros em Posse: ", bg="#303030", fg="#a202f0",
                                 font=("verdana", 10, "bold", "italic"))
        self.lb_em_posse.place(relx=0.72, rely=0.5, relwidth=0.205, relheight=0.1)

        def lb_em_posse_resp():
            self.lb_em_posse_resp = Label(self.aba2, text=self.total_livros_possuidos(), bg="#303030", fg="#f002e8",
                                          font=("verdana", 10, "bold", "italic"))
            self.lb_em_posse_resp.place(relx=0.96, rely=0.5, relwidth=0.035, relheight=0.1)
        lb_em_posse_resp()

    def __aba2_ButtonCanvas(self) -> None:
        self.canvas_aba2 = Canvas(self.aba2, bd=1, bg="#303030", highlightthickness=5, highlightbackground="#303030")
        self.canvas_aba2.place(relx=0.7, rely=0, relwidth=0.30, relheight=1)

    def widget_aba2(self) -> None:
        self.__aba2_ButtonCanvas()
        self.__aba2_LabelEntryDropDown()

    def menus(self) -> None:
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        menubar.add_cascade(label="Ordenar", menu=filemenu)
        menubar.add_cascade(label="Sair", menu=filemenu2)

        filemenu.add_command(label="Nome Cres.", command=self.set_tipo_nome)
        filemenu.add_command(label="Nota Decr.", command=self.set_tipo_notaDESC)
        filemenu.add_command(label="Autor Cres.", command=self.set_tipo_autorASC)
        filemenu2.add_command(label="Sair", command=self.janela.destroy)

    def validaEntrada(self) -> None:
        self.valida_nota = (self.janela.register(self.nota_entry), "%P")
        self.valida_posse = (self.janela.register(self.posse_entry), "%P")


if __name__ == "__main__":
    Application()

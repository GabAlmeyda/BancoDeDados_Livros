from tkinter import *
from tkinter import ttk


def bp_application(janela_bp):
    janela_bp.title("Avaliação de Livros - Carregando...")
    janela_bp.configure(bg="#303030")
    janela_bp.resizable(False, False)
    centralizar_janela(janela_bp, 500, 300)
    BarraDeProgresso(janela_bp)


def fechar_janela(janela_bp) -> None:
    janela_bp.destroy()
    janela_bp.quit()


def centralizar_janela(janela: Tk, largura: int, altura: int) -> None:
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")


class BarraDeProgresso:

    def __init__(self, janela_bp) -> None:
        self.janela_bp = janela_bp
        self.progresso()
        janela_bp.mainloop()

    @staticmethod
    def __estilo_bp() -> None:
        style_progresso = ttk.Style()
        style_progresso.theme_use("default")
        style_progresso.configure("Custom.Horizontal.TProgressbar", background="#a202f0")

    def __comecar(self) -> None:
        self.progress["value"] += 1
        if self.progress["value"] < 100:
            self.janela_bp.after(30, self.__comecar)
        else:
            fechar_janela(self.janela_bp)

    def progresso(self) -> None:
        self.__estilo_bp()
        self.progress = ttk.Progressbar(self.janela_bp, orient=HORIZONTAL, length=300, mode="determinate",
                                        style="Custom.Horizontal.TProgressbar")
        self.progress.pack(pady=140)
        self.progress["value"] = 0
        lb_carregando = Label(self.janela_bp, text="Carregando. Aguarde.", bg="#303030", fg="#a202f0", font=("verdana", 10, "bold"))
        lb_carregando.place(relx=0.35, rely=0.35, relwidth=0.32, relheight=0.1)
        self.__comecar()


if __name__ == "__main__":
    bp_application(Tk())

from tkinter import *


class EntPlaceHolder(Entry):

    def __init__(self, master=None, placeholder="PLACEHOLDER", color="gray", bg="#404040",
                 font=("verdana", 8, "bold"), validate="key", validatecommand="", fg="light gray") -> None:
        super().__init__(master)
        self.estado = True
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = fg
        self.validate = validate
        self.validatecommand = validatecommand
        self["bg"] = bg
        self["font"] = font
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self) -> None:
        self["validate"] = "none"
        self["validatecommand"] = "none"
        self["fg"] = self.placeholder_color
        self.insert(0, self.placeholder)
        self.estado = True

    def foc_in(self, *args) -> None:
        self.estado = False
        self["validate"] = self.validate
        self["validatecommand"] = self.validatecommand
        if self["fg"] == self.placeholder_color:
            self.delete(0, END)
            self["fg"] = self.default_fg_color

    def foc_out(self, *args) -> None:
        if not self.get():
            self.estado = True
            self.put_placeholder()


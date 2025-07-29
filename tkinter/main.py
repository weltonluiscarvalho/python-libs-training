from tkinter import *
from tkinter import ttk

class AtributoDominioBox:
    def __init__(self, parent):
        frame = ttk.Frame(parent)
        frame.grid()
        categoria_label = ttk.Label(frame, text="Categoria")
        categoria_label.grid(column=0, row=0)
        dominio_categoria_label = ttk.Label(frame, text="Dominio Categoria")
        dominio_categoria_label.grid(column=1, row=0)

        valor_categoria_combo_box = StringVar(value="Nome")
        categoria_combo_box = ttk.Combobox(frame, values=["Nome", "Idade", "Altura"], textvariable=valor_categoria_combo_box)
        categoria_combo_box.grid(column=0, row=1)

        valor_dominio_categoria_combo_box = StringVar(value="Jason")
        dominio_categoria_combo_box = ttk.Combobox(frame, values=["Jason", "Michael", "Peter", "Paul"], textvariable=valor_dominio_categoria_combo_box)
        dominio_categoria_combo_box.grid(column=1, row=1)

root = Tk()
atributo_dominio_box = AtributoDominioBox(root)
atributo_dominio_box = AtributoDominioBox(root)
root.mainloop()

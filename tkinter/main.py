from tkinter import *
from tkinter import ttk
from tela_inicial import TelaInicial

class AtributoDominioBox:
    def __init__(self, parent):
        frame = ttk.Frame(parent)
        frame.grid()
        frame['relief'] = 'sunken'
        frame['borderwidth'] = 2
        frame['padding'] = 10
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
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar

menu_home = Menu(menubar)
menu_atendimento = Menu(menubar)
menubar.add_cascade(menu=menu_home, label="Home")
menubar.add_cascade(menu=menu_atendimento, label="Atendimento")

menu_atendimento.add_command(label="Pendencias")
menu_atendimento.add_command(label="Habilidades")
# atributo_dominio_box = AtributoDominioBox(root)
# atributo_dominio_box = AtributoDominioBox(root)
tela_inicial = TelaInicial(root)
tela_inicial.grid()
root.mainloop()

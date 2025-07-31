from tkinter import *
from tkinter import ttk
from tela_inicial import GerenciadorTelas

root = Tk()
gerenciador_telas = GerenciadorTelas(root)
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar

menu_home = Menu(menubar)
menu_atendimento = Menu(menubar)
menubar.add_cascade(menu=menu_home, label="Home")
menubar.add_cascade(menu=menu_atendimento, label="Atendimento")

menu_atendimento.add_command(label="Pendencias")
menu_atendimento.add_command(label="Habilidades")
root.mainloop()

from tkinter import *
from tkinter import ttk
# import ttkbootstrap as ttkb
# import ttkbootstrap.constants as ttkb_const
from tela_inicial import GerenciadorTelas



root = Tk() 
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.minsize(500, 800)
root.maxsize(500, 800)
gerenciador_telas = GerenciadorTelas(root)
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar

menu_telas = Menu(menubar)
menubar.add_cascade(menu=menu_telas, label="Telas")
menu_telas.add_command(label="Cadastrar Tipo Uso", command=lambda: gerenciador_telas.alterar_tela_atual("TelaCadastrarTipoUso"))
menu_telas.add_command(label="Listar Tipo Uso", command=lambda: gerenciador_telas.alterar_tela_atual("TelaListarTipoUso"))
menu_telas.add_command(label="Cadastrar Tipo Vestimenta", command=lambda: gerenciador_telas.alterar_tela_atual("TelaCadastrarTipoVestimenta"))
menu_telas.add_command(label="Cadastrar Tipo Lavagem", command=lambda: gerenciador_telas.alterar_tela_atual("TelaCadastrarTipoLavagem"))
menu_telas.add_command(label="Cadastrar Tecido", command=lambda: gerenciador_telas.alterar_tela_atual("TelaCadastrarTecido"))
root.mainloop()

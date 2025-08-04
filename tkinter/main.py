from tkinter import *
from tkinter import ttk
from tela_inicial import GerenciadorTelas

root = Tk()
gerenciador_telas = GerenciadorTelas(root)
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar

menu_telas = Menu(menubar)
menubar.add_cascade(menu=menu_telas, label="Telas")
menu_telas.add_command(label="Cadastrar Tipo Uso", command=lambda: gerenciador_telas.alterar_tela_atual("TelaCadastrarTipoUso"))
menu_telas.add_command(label="Cadastrar Tipo Vestimenta", command=lambda: gerenciador_telas.alterar_tela_atual("TelaCadastrarTipoVestimenta"))
menu_telas.add_command(label="Cadastrar Tipo Lavagem", command=lambda: gerenciador_telas.alterar_tela_atual("TelaCadastrarTipoLavagem"))
root.mainloop()

from tkinter import *
from tkinter import ttk

class TelaInicial(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.botao_cadastrar_habilidades = ttk.Button(self, text="Cadastrar Habilidades", command=self.cadastrar_habilidades)
        self.botao_cadastrar_habilidades.grid(row=0, pady=10)

        self.botao_consultar_habilidades = ttk.Button(self, text="Consultar Habilidades", command=self.consultar_habilidades)
        self.botao_consultar_habilidades.grid(row=1, pady=10)

    def cadastrar_habilidades(self):
        print("Cadastrando habilidades")

    def consultar_habilidades(self):
        print("Consultando habilidades...")



class TelaCadastrarHabilidades(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_nome_habilidade = ttk.Label(self, text="Nome Habilidade")
        self.label_nome_habilidade.grid(row=0, column=0)

        self.variable_entry_nome_habilidade = StringVar()
        self.entry_nome_habilidade = ttk.Entry(self, textvariable=self.variable_entry_nome_habilidade)
        self.entry_nome_habilidade.grid(row=1, column=0)

        self.label_descricao_habilidade = ttk.Label(self, text="Descricao Habilidade")
        self.label_descricao_habilidade.grid(row=2, column=0)

        self.variable_entry_descricao_habilidade = StringVar()
        self.entry_descricao_habilidade = ttk.Entry(self, textvariable=self.variable_entry_descricao_habilidade)
        self.entry_descricao_habilidade.grid(row=3, column=0)


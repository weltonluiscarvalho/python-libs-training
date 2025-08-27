import tkinter as tk 
from tkinter import StringVar
import tkinter.ttk as ttk
from datetime import datetime
import db

class TelaCadastrarTecido(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.label_nome_tecido = ttk.Label(self, text="Nome do tecido")
        self.label_nome_tecido.grid(row=0, column=0)

        self.variable_entry_nome_tecido = StringVar()
        self.entry_nome_tecido = ttk.Entry(self, textvariable=self.variable_entry_nome_tecido)
        self.entry_nome_tecido.grid(row=1, column=0)

        self.label_descricao_tecido = ttk.Label(self, text="Descricao do tecido")
        self.label_descricao_tecido.grid(row=2, column=0)

        self.variable_entry_descricao_tecido = StringVar()
        self.entry_descricao_tecido = ttk.Entry(self, textvariable=self.variable_entry_descricao_tecido)
        self.entry_descricao_tecido.grid(row=3, column=0)

        self.botao_cadastrar_tecido = ttk.Button(self, text="Cadastrar", command=self.cadastrar_tecido)
        self.botao_cadastrar_tecido.grid(row=4, pady=10)
          
        self.botao_voltar = ttk.Button(self, text="Voltar para tela inicial", command=self.voltar_tela_inicial)
        self.botao_voltar.grid(row=5, pady=10)

    def cadastrar_tecido(self):
        nome = self.variable_entry_nome_tecido.get()
        descricao = self.variable_entry_descricao_tecido.get()
        data_inclusao = datetime.now().strftime("%d/%m/%Y")
        db.insert_tecido(nome, descricao, data_inclusao)
        print("Tecido Cadastrado com sucesso!")

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

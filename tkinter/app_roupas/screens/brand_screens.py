import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import StringVar
import db
from datetime import datetime

class TelaCadastrarMarca(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.label_nome_marca = ttk.Label(self, text="Nome da marca")
        self.label_nome_marca.pack(expand=True, anchor='s')

        self.entry_nome_marca_variable = StringVar()
        self.entry_nome_marca = ttk.Entry(self, textvariable=self.entry_nome_marca_variable)
        self.entry_nome_marca.pack(expand=True, anchor='n')

        self.button_cadastrar_marca = ttk.Button(self, text="Cadastrar", command=self.cadastrar_marca)
        self.button_cadastrar_marca.pack(expand=True)


    def cadastrar_marca(self):
        data_inclusao = datetime.now().strftime("%d/%m/%Y")
        nome = self.entry_nome_marca_variable.get()  
        db.insert_marca(nome, data_inclusao)

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

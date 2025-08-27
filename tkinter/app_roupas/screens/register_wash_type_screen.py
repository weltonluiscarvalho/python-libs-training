import tkinter as tk
from tkinter import StringVar
import tkinter.ttk as ttk
from datetime import datetime
import db

class TelaCadastrarTipoLavagem(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.label_descricao_tipo_lavagem = ttk.Label(self, text="Tipo da lavagem")
        self.label_descricao_tipo_lavagem.grid(row=0, column=0)

        self.variable_entry_descricao_tipo_lavagem = StringVar()
        self.entry_descricao_tipo_lavagem = ttk.Entry(self, textvariable=self.variable_entry_descricao_tipo_lavagem)
        self.entry_descricao_tipo_lavagem.grid(row=1, column=0)

        self.botao_cadastrar_descricao_tipo_uso = ttk.Button(self, text="Cadastrar", command=self.cadastrar_tipo_lavagem)
        self.botao_cadastrar_descricao_tipo_uso.grid(row=4, pady=10)
          
        self.botao_consultar_habilidades = ttk.Button(self, text="Voltar para tela inicial", command=self.voltar_tela_inicial)
        self.botao_consultar_habilidades.grid(row=5, pady=10)

    def cadastrar_tipo_lavagem(self):
        descricao = self.variable_entry_descricao_tipo_lavagem.get()
        data_inclusao = datetime.now().strftime("%d/%m/%Y")
        db.insert_tipo_lavagem(descricao, data_inclusao)
        print("Tipo lavagem Cadastrado com sucesso!")

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

from tkinter import StringVar, IntVar
import tkinter.ttk as ttk
import db

class TelaCadastrarTipoVestimenta(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.label_nome_tipo_vestimenta = ttk.Label(self, text="Tipo da vestimenta")
        self.label_nome_tipo_vestimenta.grid(row=0, column=0)

        self.variable_entry_nome_tipo_vestimenta = StringVar()
        self.entry_nome_tipo_vestimenta = ttk.Entry(self, textvariable=self.variable_entry_nome_tipo_vestimenta)
        self.entry_nome_tipo_vestimenta.grid(row=1, column=0)

        self.label_quantidade = ttk.Label(self, text="Quantidade")
        self.label_quantidade.grid(row=2, column=0)

        self.variable_entry_quantidade = IntVar()
        self.entry_quantidade = ttk.Entry(self, textvariable=self.variable_entry_quantidade)
        self.entry_quantidade.grid(row=3, column=0)

        self.botao_cadastrar_descricao_tipo_uso = ttk.Button(self, text="Cadastrar", command=self.cadastrar_tipo_vestimenta)
        self.botao_cadastrar_descricao_tipo_uso.grid(row=4, pady=10)
          
        self.botao_consultar_habilidades = ttk.Button(self, text="Voltar para tela inicial", command=self.voltar_tela_inicial)
        self.botao_consultar_habilidades.grid(row=5, pady=10)

    def cadastrar_tipo_vestimenta(self):
        descricao = self.variable_entry_nome_tipo_vestimenta.get()
        quantidade_tipo_vestimenta = self.variable_entry_quantidade.get()
        db.insert_tipo_vestimenta(descricao, quantidade_tipo_vestimenta)
        print("Tipo vestimenta Cadastrado com sucesso!")

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

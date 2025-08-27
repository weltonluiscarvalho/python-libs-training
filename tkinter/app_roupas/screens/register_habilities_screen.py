from tkinter import StringVar
import tkinter.ttk as ttk

class TelaCadastrarHabilidades(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
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
          
        self.botao_consultar_habilidades = ttk.Button(self, text="Voltar para tela inicial", command=self.voltar_tela_inicial)
        self.botao_consultar_habilidades.grid(row=4, pady=10)

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

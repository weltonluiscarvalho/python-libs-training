from tkinter import *
from tkinter import ttk


class GerenciadorTelas(ttk.Frame):

    # Como o Widget precisa saber o pai no momento da criacao, o gerenciador de telas deve criar o widget, ai fica a questão
    # como o gerenciador de telas, trocara a tela atual? Ele destruira a tela atual, e criara outra? Ou ele apenas coloca a outra
    # sobreposta? Ou ele apenas retira a visibilidade de uma tela e mostra a de tras?
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.telas = dict()
        self.tela_atual = None

    def mudar_tela(self, tela):
        self.tela_atual = tela

    def adicionar_tela_lista(self, nome_tela, tela):
        self.telas[nome_tela] = tela

    def remover_tela_lista(self, nome_tela):
        self.telas.pop(nome_tela)

    def atualizar_lista_telas(self):
        print(self.grid_info())

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


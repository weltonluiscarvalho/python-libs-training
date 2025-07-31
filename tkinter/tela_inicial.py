from tkinter import *
from tkinter import ttk


class GerenciadorTelas:

    def __init__(self, parent) -> None:
        self.telas = dict()

        for ClasseTela in (TelaInicial, TelaCadastrarHabilidades):
            objeto_tela = ClasseTela(parent, self)
            self.telas[ClasseTela.__name__] = objeto_tela
            objeto_tela.grid(row=0, column=0, sticky="nsew")

        self.alterar_tela_atual('TelaInicial')

    def alterar_tela_atual(self, nome_tela):
        if nome_tela in self.telas.keys():
            self.tela_atual = self.telas[nome_tela]
            self.tela_atual.tkraise()

class TelaInicial(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.botao_cadastrar_habilidades = ttk.Button(self, text="Cadastrar Habilidades", command=self.cadastrar_habilidades)
        self.botao_cadastrar_habilidades.grid(row=0, pady=10)

        self.botao_consultar_habilidades = ttk.Button(self, text="Consultar Habilidades", command=self.consultar_habilidades)
        self.botao_consultar_habilidades.grid(row=1, pady=10)

    def cadastrar_habilidades(self):
        print("Cadastrando habilidades")
        self.gerenciador.alterar_tela_atual('TelaCadastrarHabilidades')

    def consultar_habilidades(self):
        print("Consultando habilidades...")



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

class AtributoDominioBox:
    def __init__(self, parent):
        frame = ttk.Frame(parent)
        frame.grid()
        frame['relief'] = 'sunken'
        frame['borderwidth'] = 2
        frame['padding'] = 10
        categoria_label = ttk.Label(frame, text="Categoria")
        categoria_label.grid(column=0, row=0)
        dominio_categoria_label = ttk.Label(frame, text="Dominio Categoria")
        dominio_categoria_label.grid(column=1, row=0)

        valor_categoria_combo_box = StringVar(value="Nome")
        categoria_combo_box = ttk.Combobox(frame, values=["Nome", "Idade", "Altura"], textvariable=valor_categoria_combo_box)
        categoria_combo_box.grid(column=0, row=1)

        valor_dominio_categoria_combo_box = StringVar(value="Jason")
        dominio_categoria_combo_box = ttk.Combobox(frame, values=["Jason", "Michael", "Peter", "Paul"], textvariable=valor_dominio_categoria_combo_box)
        dominio_categoria_combo_box.grid(column=1, row=1)


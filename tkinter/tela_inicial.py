from tkinter import *
from tkinter import ttk
import db
from datetime import datetime

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
        # data_inclusao = datetime.now().strftime("%d/%m/%y")
        db.insert_tipo_vestimenta(descricao, quantidade_tipo_vestimenta)
        print("Tipo vestimenta Cadastrado com sucesso!")

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

class TelaCadastrarTipoUso(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.label_descricao_tipo_uso = ttk.Label(self, text="Descricao Tipo Uso")
        self.label_descricao_tipo_uso.grid(row=0, column=0)

        self.variable_entry_descricao_tipo_uso = StringVar()
        self.entry_descricao_tipo_uso = ttk.Entry(self, textvariable=self.variable_entry_descricao_tipo_uso)
        self.entry_descricao_tipo_uso.grid(row=1, column=0)

        self.botao_cadastrar_descricao_tipo_uso = ttk.Button(self, text="Cadastrar", command=self.cadastrar_tipo_uso)
        self.botao_cadastrar_descricao_tipo_uso.grid(row=2, pady=10)
          
        self.botao_consultar_habilidades = ttk.Button(self, text="Voltar para tela inicial", command=self.voltar_tela_inicial)
        self.botao_consultar_habilidades.grid(row=3, pady=10)

    def cadastrar_tipo_uso(self):
        descricao = self.variable_entry_descricao_tipo_uso.get()
        data_inclusao = datetime.now().strftime("%d/%m/%Y")
        db.insert_tipo_uso(descricao, data_inclusao)
        print("tipo uso inserido com sucesso")

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

class GerenciadorTelas:

    def __init__(self, parent) -> None:
        self.telas = dict()

        for ClasseTela in (TelaInicial, TelaCadastrarHabilidades, TelaCadastrarTipoUso, TelaCadastrarTipoVestimenta):
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


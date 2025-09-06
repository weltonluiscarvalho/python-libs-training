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


class TelaListarMarca(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.treeview = ttk.Treeview(self, columns=("id", "nome", "data_cadastro"), show="headings")
        # self.treeview.heading("id", text="ID")
        self.treeview.heading("nome", text="Nome")
        self.treeview.heading("data_cadastro", text="Data Cadastro")
        self.scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=self.scrollbar.set)
        marcas = db.list_marcas()

        for marca in marcas:
            item = self.treeview.insert("", "end", text=marca[1])

            self.treeview.set(item, "id", marca[0])
            self.treeview.set(item, "nome", marca[1])
            self.treeview.set(item, "data_cadastro", marca[2])
            # deletar_button = ttk.Button(self.treeview, text="X", width=2, command=lambda i=item: self.delete_item(i))


        self.treeview.pack()
        self.scrollbar.pack(fill=tk.BOTH)

        self.botao_apagar = ttk.Button(self, text="Apagar selecionado", command=self.delete_item)
        self.botao_apagar.pack(side="top")

    def delete_item(self):
        # self.treeview.delete(item)
        print(self.treeview.selection())
        item = self.treeview.item(self.treeview.selection()[0])
        print(item["values"])
        self.treeview.delete(self.treeview.selection()[0])
        db.delete_marca(item["values"][0])

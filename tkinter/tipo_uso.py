import tkinter as tk
from tkinter import ttk
from datetime import datetime
import db

class TelaListarTipoUso(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.treeview = ttk.Treeview(self, columns=("id", "descricao", "data_cadastro"), show="headings")
        self.treeview.heading("id", text="ID")
        self.treeview.heading("descricao", text="Descrição")
        self.treeview.heading("data_cadastro", text="Data Cadastro")
        self.scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=self.scrollbar.set)
        tipos_usos = db.list_tipo_uso()


        for tipo_uso in tipos_usos:
            item = self.treeview.insert("", "end", text=tipo_uso[1])

            self.treeview.set(item, "id", tipo_uso[0])
            self.treeview.set(item, "descricao", tipo_uso[1])
            self.treeview.set(item, "data_cadastro", tipo_uso[2])
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
        db.delete_tipo_uso(item["values"][0])


class TelaCadastrarTipoUso(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.frame_place_holder_top = ttk.Frame(self, relief='sunken', borderwidth=2)
        self.frame_place_holder_top.grid(row=0, column=0)
        self.label_descricao_tipo_uso = ttk.Label(self, text="Descricao Tipo Uso", anchor='center', font='TimesNewRoman 25 italic')
        self.label_descricao_tipo_uso.grid(row=1, column=0, sticky='nwse', padx=80)

        self.variable_entry_descricao_tipo_uso = tk.StringVar()
        self.entry_descricao_tipo_uso = ttk.Entry(self, textvariable=self.variable_entry_descricao_tipo_uso)
        self.entry_descricao_tipo_uso.grid(row=2, column=0, sticky='we', padx=80)

        self.botao_cadastrar_descricao_tipo_uso = ttk.Button(self, text="Cadastrar", command=self.cadastrar_tipo_uso)
        self.botao_cadastrar_descricao_tipo_uso.grid(row=3, pady=10, sticky='nwse', padx=80)
          
        self.botao_consultar_habilidades = ttk.Button(self, text="Voltar para tela inicial", command=self.voltar_tela_inicial)
        self.botao_consultar_habilidades.grid(row=4, pady=10, sticky='nwse', padx=80)

        self.frame_place_holder_bottom = ttk.Frame(self)
        self.frame_place_holder_bottom.grid(row=5, column=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=6)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=6)

    def cadastrar_tipo_uso(self):
        descricao = self.variable_entry_descricao_tipo_uso.get()
        data_inclusao = datetime.now().strftime("%d/%m/%Y")
        db.insert_tipo_uso(descricao, data_inclusao)
        print("tipo uso inserido com sucesso")

    def voltar_tela_inicial(self):
        self.gerenciador.alterar_tela_atual('TelaInicial')

import tkinter.ttk as ttk

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

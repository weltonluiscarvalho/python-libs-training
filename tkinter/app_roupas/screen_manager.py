from screens import (TelaCadastrarTecido, TelaCadastrarTipoLavagem, TelaCadastrarTipoVestimenta,
                    TelaCadastrarHabilidades, TelaInicial, TelaCadastrarTipoUso, TelaListarTipoUso)


class GerenciadorTelas:

    def __init__(self, parent) -> None:
        self.telas = dict()

        for ClasseTela in (TelaInicial, TelaCadastrarHabilidades, TelaCadastrarTipoUso, 
                           TelaCadastrarTipoVestimenta, TelaCadastrarTipoLavagem, TelaCadastrarTecido,
                           TelaListarTipoUso):
            objeto_tela = ClasseTela(parent, self)
            self.telas[ClasseTela.__name__] = objeto_tela
            objeto_tela.grid(row=0, column=0, sticky="nsew")

        self.alterar_tela_atual('TelaInicial')

    def alterar_tela_atual(self, nome_tela):
        if nome_tela in self.telas.keys():
            self.tela_atual = self.telas[nome_tela]
            self.tela_atual.tkraise()

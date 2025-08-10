import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
import ttkbootstrap.constants as ttkb_const
from ttkbootstrap.scrolled import ScrolledFrame

class HomeScreen(ttk.Frame):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)

        self.gerenciador = gerenciador
        self.internal_frame = ttkb.Frame(self)
        self.botao_registrar_uso = ttkb.Button(self.internal_frame, text='Registrar Uso', bootstyle=ttkb_const.PRIMARY)
        self.botao_registrar_uso.grid(column=0, row=1, sticky='nesw', pady=(0, 30))

        self.botao_registrar_vestimenta = ttkb.Button(self.internal_frame, text='Registrar Vestimenta', bootstyle=ttkb_const.PRIMARY)
        self.botao_registrar_vestimenta.grid(column=0, row=2, sticky='nswe', pady=(0, 30))

        self.botao_consultar_uso = ttkb.Button(self.internal_frame, text='Consultar Uso', bootstyle=ttkb_const.PRIMARY)
        self.botao_consultar_uso.grid(column=0, row=3, sticky='wsen')

        self.internal_frame.columnconfigure(0, weight=1)
        # self.internal_frame.rowconfigure(0, weight=1)
        self.internal_frame.rowconfigure(1, weight=1)
        self.internal_frame.rowconfigure(2, weight=1)
        self.internal_frame.rowconfigure(3, weight=1)
        # self.internal_frame.rowconfigure(4, weight=1)
        self.internal_frame.grid(column=0, row=1, sticky='nswe', padx=50)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.columnconfigure(0, weight=1)
        self.grid(column=0, row=0, sticky='nwse')

# app = ttkb.Window(themename="darkly")
#
# sf = ScrolledFrame(app, autohide=True)
# sf.pack(fill=ttkb_const.BOTH, expand=ttkb_const.YES, padx=10, pady=10)
#
# for x in range(20):
#     ttkb.Checkbutton(sf, text=f'Checkbutton {x}').pack(anchor=ttkb_const.W)
#
# app.mainloop()

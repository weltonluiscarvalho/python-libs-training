from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttkb
import ttkbootstrap.constants as ttkb_const
from ttkbootstrap.scrolled import ScrolledFrame

# class HomeScreen(ScrolledFrame):
#     pass 

app = ttkb.Window(themename="darkly")

sf = ScrolledFrame(app, autohide=True)
sf.pack(fill=ttkb_const.BOTH, expand=ttkb_const.YES, padx=10, pady=10)

for x in range(20):
    ttkb.Checkbutton(sf, text=f'Checkbutton {x}').pack(anchor=ttkb_const.W)

app.mainloop()

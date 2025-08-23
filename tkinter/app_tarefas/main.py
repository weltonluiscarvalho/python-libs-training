import customtkinter as ctk
import re

def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5 


app = ctk.CTk()

app.geometry('300x500')
app.resizable(False, False)
check_num_wrapper = (app.register(check_num), '%P')

label1 = ctk.CTkLabel(master=app, text='Nome da tarefa')
label1.pack()

entry = ctk.CTkEntry(master=app)
entry.pack()

data_hora_frame = ctk.CTkFrame(master=app)
data_hora_frame.pack()

label_data = ctk.CTkLabel(master=data_hora_frame, text='data')
label_data.pack(side='left')

entry_data = ctk.CTkEntry(master=data_hora_frame, placeholder_text='22/08/2025', validate='key', validatecommand=check_num_wrapper)
entry_data.pack(side='left')

label_hora = ctk.CTkLabel(master=data_hora_frame, text='hora')
label_hora.pack(side='left')

entry_hora = ctk.CTkEntry(master=data_hora_frame)
entry_hora.pack(side='left')

app.mainloop()

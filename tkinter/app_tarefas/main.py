import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import re

def check_num(newval):
    # verify if character is numeric, if not, just end validate function
    
    print(newval)
    print(re.match('^(0[0-9]|[12][0-9]|[3][01])/(0[0-9]|1[0-2])/\\d{4}$', newval) is not None)
    return re.match('^(0[0-9]|[12][0-9]|[3][01])/(0[0-9]|1[0-2])/\\d{4}$', newval) is not None 
    # verify cursor position
    # if in a slash position, put it one character to the right
    # take the actual value of the slice between the previous slash (or 0 if the acual is the first) and the acual slash 
    # move the values of the slice one character to the left, and insert the new one in the new position opened in the right
    


app = tk.Tk()

app.geometry('300x500')
app.resizable(False, False)
check_num_wrapper = (app.register(check_num), '%P')

label1 = ttk.Label(master=app, text='Nome da tarefa')
label1.pack()

entry_variable = ctk.StringVar(value="teste")
entry = ttk.Entry(master=app, textvariable=entry_variable)
entry.pack()

# Frame that will join date and hour related widgets
# data_hora_frame = ttk.Frame(master=app)
# data_hora_frame.pack()


entry_data_frame = ttk.Frame(master=app)
entry_data_frame.rowconfigure((0,1), weight=1, uniform='a')
entry_data_frame.columnconfigure((0,2,3), weight=1, uniform='a')
entry_data_frame.columnconfigure(1, weight=3, uniform='a')
entry_data_frame.pack(side='left', padx=20)

label_data = ttk.Label(master=entry_data_frame, text='data', anchor='center')
label_data.grid(column=0, row=0, sticky='news')

entry_data_variable = tk.StringVar()
entry_data = ttk.Entry(master=entry_data_frame, textvariable=entry_data_variable, validate='focusout', validatecommand=check_num_wrapper)
entry_data.grid(column=1, row=0, sticky='news')

entry_data_error_label = ttk.Label(master=entry_data_frame, text='a data deve estar\n no formato dd/mm/aaaa')
entry_data_error_label.grid(column=1, row=1, sticky='news')

label_hora = ttk.Label(master=entry_data_frame, text='hora', anchor='center')
label_hora.grid(column=2, row=0, sticky='news')

entry_hora_variable = tk.StringVar(value='12:20')
entry_hora = ttk.Entry(master=entry_data_frame, textvariable=entry_hora_variable)
entry_hora.grid(column=3, row=0, sticky='news')

app.mainloop()

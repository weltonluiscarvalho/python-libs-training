from ast import UnaryOp, main
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

main_frame = ttk.Frame(app)
main_frame.pack(expand=True)

register_task_frame = ttk.Frame(main_frame)
register_task_frame.columnconfigure((0), weight=2, uniform='a')
register_task_frame.columnconfigure((1), weight=1, uniform='a')
register_task_frame.rowconfigure((0,1), weight=1, uniform='a')
register_task_frame.pack(padx=20, expand=True)
list_task_frame = ttk.Frame(main_frame)
list_task_frame.pack(expand=True, fill='both')

task_name_label = ttk.Label(master=register_task_frame, text='Nome da tarefa')
task_name_label.grid(column=0, row=0, columnspan=5, sticky='w')

task_name_entry_variable = ctk.StringVar()
task_name_entry = ttk.Entry(master=register_task_frame, textvariable=task_name_entry_variable)
task_name_entry.grid(column=0, row=1, columnspan=5, sticky='ew')

#########################################################################################
task_data_frame = ttk.Frame(register_task_frame)
task_data_frame.grid(column=0, row=2, padx=(0,10), pady=(20,0))

task_data_label = ttk.Label(master=task_data_frame, text='data', anchor='center')
task_data_label.pack(side='left')

task_data_entry_variable = tk.StringVar()
task_data_entry = ttk.Entry(master=task_data_frame, textvariable=task_data_entry_variable, validate='focusout', validatecommand=check_num_wrapper)
task_data_entry.pack(side='left')

entry_data_error_label = ttk.Label(master=register_task_frame, text='a data deve estar\n no formato dd/mm/aaaa')
entry_data_error_label.grid(column=0, row=3, columnspan=2, sticky='news')

###########################################################################################

task_hour_frame = ttk.Frame(register_task_frame)
task_hour_frame.grid(column=1, row=2, pady=(20,0))

task_hour_label = ttk.Label(master=task_hour_frame, text='hora', anchor='center')
task_hour_label.pack(side='left')

task_hour_entry_variable = tk.StringVar(value='12:20')
task_hour_entry = ttk.Entry(master=task_hour_frame, textvariable=task_hour_entry_variable)
task_hour_entry.pack(side='left')

app.mainloop()

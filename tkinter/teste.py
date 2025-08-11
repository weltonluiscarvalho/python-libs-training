import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

style = ttk.Style()
style.configure('frame1.TFrame', background='blue', relief='sunken')
style.configure('frame2.TFrame', background='red', relief='sunken')
frame1 = ttk.Frame(root, style='frame1.TFrame', borderwidth=2)
frame1.pack()

frame2 = ttk.Frame(frame1, style='frame2.TFrame', borderwidth=2)
frame2.pack()

frame3 = ttk.Frame(frame1)
frame3.pack()

button1 = ttk.Button(frame2, text='Button 1')
label1 = ttk.Label(frame2, text='Label 1')
button2 = ttk.Button(frame2, text='Button 2')
label2 = ttk.Label(frame2, text='Label 2')
button3 = ttk.Button(frame2, text='Button 3')
label3 = ttk.Label(frame2, text='Label 3')
button4 = ttk.Button(frame2, text='Button 4')
label4 = ttk.Label(frame2, text='Label 4')

def button_1():
    if not button1.winfo_manager():
        button1.pack(side='left', expand=False)
    else:
        button1.pack_forget()

def label_1():
    if not label1.winfo_manager():
        label1.pack(side='top', expand=False)
    else:
        label1.pack_forget()

def button_2():
    if not button2.winfo_manager():
        button2.pack(side='right', expand=False)
    else:
        button2.pack_forget()

def label_2():
    if not label2.winfo_manager():
        label2.pack(side='bottom', expand=False)
    else:
        label2.pack_forget()

def button_3():
    if not button3.winfo_manager():
        button3.pack(side='left', expand=False)
    else:
        button3.pack_forget()

def label_3():
    if not label3.winfo_manager():
        label3.pack(side='top', expand=False)
    else:
        label3.pack_forget()

def button_4():
    if not button4.winfo_manager():
        button4.pack(side='right', expand=False)
    else:
        button4.pack_forget()

def label_4():
    if not label4.winfo_manager():
        label4.pack(side='bottom', expand=False)
    else:
        label4.pack_forget()


b1 = ttk.Button(frame3, text='Invert Button 1', command=button_1)
b2 = ttk.Button(frame3, text='Invert Button 2', command=button_2)
b3 = ttk.Button(frame3, text='Invert Button 3', command=button_3)
b4 = ttk.Button(frame3, text='Invert Button 4', command=button_4)
b5 = ttk.Button(frame3, text='Invert Label 1', command=label_1)
b6 = ttk.Button(frame3, text='Invert Label 2', command=label_2)
b7 = ttk.Button(frame3, text='Invert Label 3', command=label_3)
b8 = ttk.Button(frame3, text='Invert Label 4', command=label_4)

b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)
b4.grid(row=0, column=4)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)
b8.grid(row=1, column=4)

# root.after(10000, button_1)
# root.after(20000, label_1)
# root.after(30000, button_2)
# root.after(40000, label_2)
# root.after(50000, button_3)
# root.after(60000, label_3)
# root.after(70000, button_4)
# root.after(80000, label_4)

root.mainloop()

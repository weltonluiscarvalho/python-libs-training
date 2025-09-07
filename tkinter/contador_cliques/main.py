import tkinter as tk
from tkinter import IntVar

contador = 0

def resetar():
    global contador
    contador = 0
    label_variable.set(contador)
    if contador < 10:
        label.configure(fg="black")

def incrementar():
    global contador
    contador += 1
    label_variable.set(contador)
    if contador >= 10:
        label.configure(fg="blue")

janela = tk.Tk()
janela.title("contador de cliques")

label_variable = IntVar(value=0)
label = tk.Label(janela, textvariable=label_variable, font=("Arial", 30))
label.pack(pady=20)

botao = tk.Button(janela, text="Clique aqui", command=incrementar, font=("Arial", 15))
botao.pack(pady=10)

botao = tk.Button(janela, text="Resetar", command=resetar, font=("Arial", 15))
botao.pack(pady=10)

janela.mainloop()

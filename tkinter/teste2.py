import tkinter as tk

def move_button():
    x, y = button.winfo_x(), button.winfo_y()
    if x < 300:
        button.place(x=x + 1, y=y)
        root.after(10, move_button)

root = tk.Tk()
root.geometry("400x200")

button = tk.Button(root, text="Mover", command=move_button)
button.place(x=0, y=50)

root.mainloop()

import tkinter as tk
from tkinter import ttk



window = tk.Tk()
 
lbl_inicio = ttk.Label(window, text='Prueba de eventos')
lbl_inicio.grid(column=0, row=0)

selected = tk.StringVar()
lbl_boton = ttk.Label(window, text='')
lbl_boton.grid(column=0, row=4)

def limpiar():
    selected.set(None)
    lbl_boton.config(text='')

def cambiar_texto():
    lbl_boton.config(text=f'Opción {selected.get()}')

r1 = ttk.Radiobutton(window, text='Opción 1', value=1, variable=selected, command=cambiar_texto)
r2 = ttk.Radiobutton(window, text='Opción 2', value=2, variable=selected, command=cambiar_texto)
r3 = ttk.Radiobutton(window, text='Opción 3', value=3, variable=selected, command=cambiar_texto)

r1.grid(column=0, row=1)
r2.grid(column=0, row=2)
r3.grid(column=0, row=3)

'''
r1.bind('<Double-1>', cambiar_texto)
r2.bind('<Double-1>', cambiar_texto)
r3.bind('<Double-1>', cambiar_texto)'''

btn_limpiar = ttk.Button(window, text='Limpiar', command=limpiar)
btn_limpiar.grid(column=1, row=4)

window.mainloop()

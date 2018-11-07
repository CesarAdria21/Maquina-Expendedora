import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
entrada = tk.Entry(ventana)
entrada.pack(fill = tk.X , padx = 5, pady = 5 , ipadx = 5 , ipady = 5)

def validar():
    if entrada.get() == 'josep':
        abrirventana2()
    else:
        messagebox.showwarning("Password Incorrecto")

def abrirventana2():
    
    ventana.withdraw()

    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('380x300+1900+100')
    win.configure(background='dark green')
    e3 = tk.Label(win , text = "Segunda ventana", bg ="blue", fg ="white")
    e3.pack( padx = 5, pady = 5 , ipadx = 5 , ipady = 5, fill = tk.X)

    boton2 = tk.Button(win, text='OK', command = win.destroy)
    boton2.pack( side = tk.TOP)

def cerraventana():
    
    ventana.destroy()

    ventana.title("Ventana 1")
    ventana.geometry('380x300')
    ventana.configure(background='dark green')

    el = tk.Label(ventana, text = "Password:", bg="pink", fg="white")
    el.pack( padx = 5, pady = 5 , ipadx = 5 , ipady = 5)

boton = tk.Button(ventana, text="Nueva ventana", fg = "blue" , command = abrirventana2)
boton.pack(side = tk.TOP)

boton3 = tk.Button(ventana, text="Validar Password", fg = "blue" , command = abrirventana2)
boton3.pack(side = tk.TOP)
ventana.mainloop()

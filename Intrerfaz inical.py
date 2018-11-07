import tkinter as tk
from tkinter import messagebox
from tkinter import *

def Password():
    contra = Toplevel()
    contra.title("Password")
    contra.geometry('380x300')
    e3 = tk.Label(contra , text = "Segunda ventana", bg ="blue", fg ="white")
    e3.pack( padx = 5, pady = 5 , ipadx = 5 , ipady = 5, fill = tk.X)
    contra.mainloop

def Compra():
    contra = Toplevel()
    contra.title("Compra")
    contra.mainloop


raiz=Tk()
raiz.title("Maquina Expendedora")
raiz.resizable(False,True)
raiz.config(bg="white")

miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()
Label(miFrame, text="Ingrese tipo de usuario : ", fg="black" , font=(18)).place(x=20,y=20)
miFrame.config(bg="light blue")

botonAdministrador = Button(raiz,text=" Administrador ",command = Password)
botonAdministrador.place(x=20,y=60)

botonConsumidor = Button(raiz,text=" Consumidor ", command = Compra)
botonConsumidor.place(x=160,y=60)

raiz.mainloop()
from tkinter import *

raiz=Tk()
raiz.title("Maquina Expendedora")
raiz.resizable(False,True)
raiz.config(bg="white")
raiz.iconbitmap("ARB.ico")

miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()
Label(miFrame, text="Ingrese tipo de usuario : ", fg="black" , font=(18)).place(x=20,y=20)
miFrame.config(bg="light blue")

raiz.mainloop()
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

botonAdministrador = Button(raiz,text=" Administrador ")
botonAdministrador.place(x=20,y=60)

minombre=StringVar()
cuadro = Entry(miFrame, textvariable=minombre)
cuadro.grid(row=0 ,column=1 , padx=10 ,pady=0)
cuadro

cuadro.place(x=20,y=60)

def codigoAdministrador():
    minombre.set("Alvaro")

botonCliente = Button(raiz,text="   Cliente   ",command=codigoAdministrador)
botonCliente.place(x=130,y=60)

raiz.mainloop()
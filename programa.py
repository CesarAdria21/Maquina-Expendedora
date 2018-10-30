from tkinter import *

raiz=Tk()
raiz.title("Maquina Expendedora")
raiz.resizable(True,True)
raiz.config(bg="white")
raiz.iconbitmap("ARB.ico")

miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()
# Label(miFrame, text="Ingrese tipo de usuario : ", fg="black" , font=(18)).place(x=20,y=20)
miFrame.config(bg="black")

botonAdmistrador = Button(raiz, text= "Admistrador")
botonAdmistrador.pack()
botonUsuario = Button(raiz, text= "Usuario")
botonUsuario.pack()

pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black")

boton4=Button(miFrame,text="4", width=3)
boton4.grid(row=2, column=1)
boton5=Button(miFrame,text="5", width=3)
boton5.grid(row=2, column=2)
boton6=Button(miFrame,text="6", width=3)
boton6.grid(row=2, column=3)
boton1=Button(miFrame,text="1", width=3)
boton1.grid(row=1, column=1)
boton2=Button(miFrame,text="2", width=3)
boton2.grid(row=1, column=2)
boton3=Button(miFrame,text="3", width=3)
boton3.grid(row=1, column=3)


raiz.mainloop()
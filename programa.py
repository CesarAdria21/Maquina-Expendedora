from tkinter import *

raiz=Tk()
raiz.title("Maquina Expendedora")
raiz.resizable(False,False)
raiz.config(bg="black")
raiz.iconbitmap("ARB.ico")

miFrame = Frame(raiz, width=500, height=400)

miFrame.pack()


numeroPantalla = StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black",fg ="white", justify="right")

def numeroPulsado(num):
    numeroPantalla.set(num)
    
botonComprar=Button(miFrame,text="Comprar",width=3,command=lambda:numeroPulsado("Recibiendo..."))
botonComprar.grid(row=4, column=4)
botonBorrar=Button(miFrame,text="Borrar",width=3,command=lambda:numeroPulsado("a"))
botonBorrar.grid(row=3, column=4)
boton4=Button(miFrame,text="4", width=3,command=lambda:numeroPulsado("Agua mineral"))
boton4.grid(row=4, column=1)
boton5=Button(miFrame,text="5", width=3,command=lambda:numeroPulsado("Gaseosa"))
boton5.grid(row=4, column=2)
boton6=Button(miFrame,text="6", width=3,command=lambda:numeroPulsado("Red Bull"))
boton6.grid(row=4, column=3)
boton1=Button(miFrame,text="1", width=3,command=lambda:numeroPulsado("Gatorade"))
boton1.grid(row=3, column=1)
boton2=Button(miFrame,text="2", width=3,command=lambda:numeroPulsado("Cerveza"))
boton2.grid(row=3, column=2)
boton3=Button(miFrame,text="3", width=3,command=lambda:numeroPulsado("Chicha Morada"))
boton3.grid(row=3, column=3)


botonAdmistrador = Button(raiz, text= "Admistrador")
botonAdmistrador.pack()
botonUsuario = Button(raiz, text= "Usuario")
botonUsuario.pack()

raiz.mainloop()
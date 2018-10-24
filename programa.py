from tkinter import *

raiz=Tk()
raiz.title("Proyecto")
raiz.resizable(False,True)
raiz.geometry("650x350")
raiz.config(bg="white")
raiz.mainloop()

root=Tk()
miFrame = Frame(root, width=500, heigth=400)
miFrame.pack()
miLabel=Label(miFrame, text="Bebidas")
miLabel.pack()

root.mainloop()

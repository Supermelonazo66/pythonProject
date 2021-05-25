from tkinter import filedialog
from tkinter import *
import os

ventana = Tk()

def abrir_archivo():
    archivo_abierto = filedialog.askopenfilename(initialdir = "/", title = "Seleccionar archivo", filetypes = ("jpeg files","*jpg"))
    print(archivo_abierto)

Button(text="Abrir archibo", bg="pale green", command=abrir_archivo).place(x=10,y=10)


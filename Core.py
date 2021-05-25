from tkinter import filedialog
from tkinter import *
import os
import cv2
import matplotlib.pyplot as plt

ventana = Tk()

class Core:

    image = ""
    sensibility = 0

    def __init__(self, image, sensibility):
        self.image = image
        self.sensibility = sensibility

    def procesare(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, self.sensibility, self.sensibility, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        image_cont = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
        plt.imshow(image_cont)
        plt.show()

    def abrir_archivo(self):
        archivo_abierto = filedialog.askopenfilename(initialdir="/",
                                                     title="Seleccione archivo", filetypes=(("jpeg files", "*.jpg"),
                                                                                            ("all files", "*.*")))
        print(archivo_abierto)

image = Core(cv2.imread("thumbs_up_down.jpg"), 2)

image.procesare()



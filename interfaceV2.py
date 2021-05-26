import io
import os
import PySimpleGUI as sg
from PIL import Image
from Core import core

file_types = [("JPEG", "*.jpg"),
              ("PNG", "*.png"),
              ("All files", "*.*")]


layout = [
    [sg.Image(key="-IMAGE-")],
    [
         sg.Text("Image File"),
         sg.Input(size=(25, 1), key="-FILE-"),
         sg.FileBrowse(file_types=file_types),
         sg.Button("Load Image"),
    ],
    [sg.Slider(range=(0, 100), size=(50, 10), orientation="h", key="-SLIDER-")]
]

window = sg.Window("Image Viewer", layout)

sensibilitate = 1

def procesare(sensibilitate):
    img = core(values["-FILE-"], sensibilitate)
    img.procesare()
    image = Image.open("temp.jpg")
    image.thumbnail((600, 600))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["-IMAGE-"].update(data=bio.getvalue())

flag = 0

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
            break

    if event == "Load Image":
        filename = values["-FILE-"]
        if os.path.exists(filename):
            procesare(sensibilitate)
            if int(values["-SLIDER-"]) != sensibilitate:
                sensibilitate = 2.25 * int(values["-SLIDER-"])
                procesare(sensibilitate)

window.close()

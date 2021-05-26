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
        [sg.Slider(range=(0, 100), orientation="h")
        ]

    ]

window = sg.Window("Contorous Images Detection - Python", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    Img = core(values["-FILE-"], 225)
    Img.procesare()

window.close()

# Packages from Python Libraries
import PySimpleGUI as sg

# Our packages
from Nota import Nota
import tools

class WinMain():
    def __init__(self):
        layout = [
            [sg.Text("¡¡Bienvenido!!", 
             text_color=tools.TITLE_COLOR_0, font = tools.TITLE_FONT_0, 
             background_color=tools.BACKGROUND, justification = 'center')],
            [sg.Text("Si desea empezar una nota, de click en\n-Generar nota-", 
             text_color=tools.TEXT_COLOR_0, font = tools.TEXT_FONT_0, 
             background_color=tools.BACKGROUND, justification = 'center')],
            [sg.Button("Generar nota", key = "start", button_color=tools.BUTTON_GOLD)]
        ]

        self.window = sg.Window('Bienvenida', 
         layout,
         background_color=tools.BACKGROUND,
         element_justification='c')

    def display(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'start':
                break
        
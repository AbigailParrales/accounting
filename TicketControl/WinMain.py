# Packages from Python Libraries
import PySimpleGUI as sg

# Our packages
from Nota import Nota
from WinNota import WinNota
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

        self.state = 'NEW'
        self.winNota = None
        self.nota = None

    def display(self):
        self.state = 'DISPLAYING'
        while self.state != 'CLOSE':
            event, values = self.window.read()
            if event == 'start':
                self.state = 'CREATING_NOTA'
                self.window.Hide()
                self.nota = Nota()
                self.winNota = WinNota(self.nota)
                while self.winNota.display() != 'WIN_CLOSED':
                    pass
                self.state = 'END_NOTA'
                self.winNota.endNote()
                self.window.UnHide()
            if event == sg.WINDOW_CLOSED:
                self.state = 'CLOSE'

        # Loop breaked, state = CLOSE
        self.window.close()
        self.winNota = None
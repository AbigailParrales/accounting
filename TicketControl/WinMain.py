# Packages from Python Libraries
import PySimpleGUI as sg

# Our packages
from Nota import Nota
from WinNota import WinNota
from WinNotaConf import WinNotaConf
import tools.fonts as fonts

class WinMain():
    def __init__(self):
        layout = [
            [sg.Text("¡¡Bienvenido!!", 
             text_color=fonts.TITLE_COLOR_0, font = fonts.TITLE_FONT_0, 
             background_color=fonts.BACKGROUND, justification = 'center')],
            [sg.Text("Si desea empezar una nota, de click en\n-Generar nota-", 
             text_color=fonts.TEXT_COLOR_0, font = fonts.TEXT_FONT_0, 
             background_color=fonts.BACKGROUND, justification = 'center')],
            [sg.Button("Generar nota", key = "start", button_color=fonts.BUTTON_GOLD)]
        ]

        self.window = sg.Window('Bienvenida', 
         layout,
         background_color=fonts.BACKGROUND,
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
                
                winNotaConf = WinNotaConf()
                fechaNota, folioNota = winNotaConf.display()
                self.nota = Nota(fechaNota, folioNota)
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
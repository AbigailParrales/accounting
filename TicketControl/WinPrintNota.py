import PySimpleGUI as sg

import tools.fonts as fonts

class WinPrintNota():
    def __init__(self, nota):
        self.nota = nota
        layout = [
            [sg.T("Introduzca el nombre con el que \ndesea guardar su nota")],
            [sg.Input(key='route')],
            [sg.Button('Imprimir', key='print', button_color=('black', 'forest green'))],
        ]

        self.window = sg.Window(
            'Imprimir nota', layout=layout, 
            background_color=fonts.BACKGROUND)

    def display(self):
        event, values = self.window.read()
        if event == sg.WINDOW_CLOSED:
            self.window.close()
            # break
        elif event == 'print':
            self.window.close()
            return values['route']
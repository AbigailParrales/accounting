import PySimpleGUI as sg

import tools

class WinPrevNota():
    def __init__(self, nota):
        self.nota = nota
        layout = [
            [sg.T("Titulo de la nota")],
            [
                sg.Column([[sg.Text(x)] for x in self.nota.cantidades]),
                sg.Column([[sg.Text(x)] for x in self.nota.descripciones]),
                sg.Column([[sg.Text(x)] for x in self.nota.pUnitarios]),
                sg.Column([[sg.Text(x)] for x in self.nota.importes])
            ]
        ]

        self.window = sg.Window(
            'Vista previa de la nota generada', layout=layout, 
            background_color=tools.BACKGROUND)

    def display(self):
        event, values = self.window.read()
        if event == sg.WINDOW_CLOSED:
            self.window.close()
            # break
import PySimpleGUI as sg

from Nota import Nota
from WinPrevNota import WinPrevNota
import tools

class WinNota():
    def __init__(self, nota):
        layout = [
            [sg.Text("Ingrese los datos de su venta", 
             text_color=tools.TEXT_COLOR_0, font = tools.TEXT_FONT_0, 
             background_color=tools.BACKGROUND, justification = 'center')],
            [sg.Text("Cantidad", size=(15, 1)), sg.Input(key='cantidad', do_not_clear = False)],
            [sg.Text("Descripcion", size=(15, 1)), sg.Input(key='descripcion', do_not_clear = False)],
            [sg.Text("Precio unitario", size=(15, 1)), sg.Input(key='pUnit', do_not_clear = False)],
            [sg.Button('Registrar compra', key='regCompra', button_color=('black', 'forest green'))],
            [
                sg.Button('Vista previa nota', key='prevNota', button_color=('black', 'forest green')),
                sg.Button('Imprimir nota', key='printNota', button_color=('black', 'turquoise1'))
            ]
        ]

        self.window = sg.Window(
            'Registro de ventas', layout=layout, 
            background_color=tools.BACKGROUND,
            element_justification='c')
        
        self.nota = nota

    def display(self):
        event, values = self.window.read()
        if event == sg.WINDOW_CLOSED:
            return 'WIN_CLOSED'
        elif event == 'regCompra':
            self.nota.registrarVenta(int(values['cantidad']), values['descripcion'], int(values['pUnit']))
        elif event == 'prevNota':
            winPrevNota = WinPrevNota(self.nota)
            winPrevNota.display()
        elif event == 'printNota':
            print(self.nota)

    def endNote(self):
        self.window.close()
        self.Nota = None
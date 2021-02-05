import PySimpleGUI as sg

from Nota import Nota
from WinPrevNota import WinPrevNota
from WinPrintNota import WinPrintNota

import tools.fonts as fonts
import tools.print2NormalPrinter as printer

class WinNota():
    def __init__(self, nota):
        layout = [
            [sg.Text("Ingrese los datos de su venta", 
             text_color=fonts.TEXT_COLOR_0, font = fonts.TEXT_FONT_0, 
             background_color=fonts.BACKGROUND, justification = 'center')],
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
            background_color=fonts.BACKGROUND,
            element_justification='c')
        
        self.nota = nota

    def display(self):
        event, values = self.window.read()
        if event == sg.WINDOW_CLOSED:
            return 'WIN_CLOSED'
        elif event == 'regCompra':
            self.nota.registrarVenta(values['cantidad'], values['descripcion'], float(values['pUnit']))
        elif event == 'prevNota':
            winPrevNota = WinPrevNota(self.nota)
            winPrevNota.display()
        elif event == 'printNota':
            # winPrintNota = WinPrintNota(self.nota)
            # fName = winPrintNota.display()

            fPath = f"C://Projects/repos/accounting/TicketControl/Notas/Nota_{self.nota.folio}.txt"
            fileName = open(fPath, 'w+')
            fileName.write(self.nota.__str__())
            fileName.close()
            # print(self.nota)
            printer.printTxt(fPath)
            self.endNote()
            return 'WIN_CLOSED'

    def endNote(self):
        self.window.close()
        self.nota = None
import PySimpleGUI as sg

import tools.fonts as fonts

class WinNotaConf():
    def __init__(self):
        listOfDays = list(map(str, list(range(0,32))))
        listOfMonths = list(map(str, list(range(0,13))))
        listOfYears = list(map(str, list(range(2020,2023))))

        layout = [
            [sg.Text("Ingrese los datos de su nota", 
             text_color=fonts.TEXT_COLOR_0, font = fonts.TEXT_FONT_0, 
             background_color=fonts.BACKGROUND, justification = 'center')],
            [sg.T("Fecha de la nota", justification = 'center')],
            [
                sg.Text("Dia", size=(5, 1)), sg.Combo(listOfDays, key='day'),
                sg.Text("Mes", size=(5, 1)), sg.Combo(listOfMonths, key='month'),
                sg.Text("Año", size=(5, 1)), sg.Combo(listOfYears, key='year'),
            ],
            [sg.Text("Folio", size=(15, 1)), sg.Input(key='folio', do_not_clear = False)],
            [sg.Button('Listo', key='ok', button_color=('black', 'lawn green'))],
        ]

        self.window = sg.Window(
            'Imprimir nota', layout=layout, 
            background_color=fonts.BACKGROUND)

    def display(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                self.window.close()
                return None, None
            elif event == 'ok':
                self.window.close()
                fecha = f"{values['year']}-{values['month']}-{values['day']}"
                return fecha, values['folio']
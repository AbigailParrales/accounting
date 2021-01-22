import PySimpleGUI as sg
BACKGROUND = 'light yellow'

cantidades = ["Cantidad", 1, 2, 3, 4]
descripciones = ["Descripcion", 1, 2, 3, 4]
precios = ["Precios", 1, 2, 3, 4]
importes = ["Importe", 1, 2, 3, 4]

region = [
    [
        # sg.Column([[sg.Text("Cantidad")], [sg.Text("Cantidad2")]]),
        sg.Column([[sg.Text(x)] for x in cantidades]),
        sg.Column([[sg.Text(x)] for x in descripciones]),
        sg.Column([[sg.Text(x)] for x in precios]),
        sg.Column([[sg.Text(x)] for x in importes])
     ],
    # [

        # NO
        # sg.Column([sg.Text("Cantidad")]),
        # sg.Column([sg.Text("Desc")]),
        # sg.Column([sg.Text("pUnit")]),
        # sg.Column([sg.Text("Importes")])

        # SI
        # sg.Text("Cantidad"),
        # sg.Text("Desc"),
        # sg.Text("pUnit"),
        # sg.Text("Importes")

        # NO
        # [sg.Column([sg.Text("Cantidad")])],
        # [sg.Column([sg.Text("Desc")])],
        # [sg.Column([sg.Text("pUnit")])],
        # [sg.Column([sg.Text("Importes")])]
    # ],
    [sg.Text("Presiones IMPRIMIR para actualizar")]
]
 
main_window = sg.Window('Nota de venta', region, background_color=BACKGROUND)

while True:
    event, values = main_window.read()

    # See if window was closed
    if event == sg.WINDOW_CLOSED:
        # print(nota)
        break

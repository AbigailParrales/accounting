import PySimpleGUI as sg

BACKGROUND = 'light yellow'
TITLE_COLOR_0 = 'forest green'
TEXT_COLOR_0 = 'burlywood4'

BUTTON_GOLD = ['black', 'gold']


TITLE_FONT_0 = ('Helvetica',36, 'bold')
TEXT_FONT_0 = ('Helvetica',24, 'bold')

def genColumnObjs(col, width):
    newList=[]
    for row in col:
        newList.append(sg.Text(row, size=(width, 1)))
    
    return newList

def makeNota(objNota):
    # ["Cantidad", "Descripcion", "Precio Unitario", "Importe"]
    # Have 4 colums
    layout  = [
        [sg.T("Titulo de la nota")],
        [
            sg.Column([[sg.Text(x)] for x in objNota.cantidades]),
            sg.Column([[sg.Text(x)] for x in objNota.descripciones]),
            sg.Column([[sg.Text(x)] for x in objNota.pUnitarios]),
            sg.Column([[sg.Text(x)] for x in objNota.importes])
        ]
    ]

    return sg.Window('Nota de venta', layout, background_color=BACKGROUND)
import PySimpleGUI as sg

from Nota import Nota

BACKGROUND = 'light yellow'

nota = Nota()

def genColumnObjs(col, width):
    newList=[]
    for row in col:
        newList.append(sg.Text(row, size=(width, 1)))
    
    return newList

def makeNota(objNota):
    # ["Cantidad", "Descripcion", "Precio Unitario", "Importe"]
    # Have 4 colums
    cantidad = sg.Column([objNota.getCantidades()])
    descripcion = sg.Column([objNota.getDescripciones()])
    pUnit = sg.Column([objNota.getPUnitarios()])
    importe = sg.Column([objNota.getImportes()])

    return [cantidad, descripcion, pUnit, importe]



# Main window
title_region = [
    sg.Text("Nota de venta", text_color='forest green', 
     font=('Helvetica',36, 'bold'), background_color=BACKGROUND)
 ]
bottom_region = [
    sg.Button('Imprimir', key='print', button_color=('black', 'forest green'))
 ]
left_region = [
    [sg.Text("Cantidad", size=(15, 1)), sg.Input(key='cantidad', do_not_clear = False)],
    [sg.Text("Descripcion", size=(15, 1)), sg.Input(key='descripcion', do_not_clear = False)],
    [sg.Text("Precio unitario", size=(15, 1)), sg.Input(key='pUnit', do_not_clear = False)],
    [sg.Button('Registrar compra', key='compra', button_color=('black', 'forest green'))]
 ]
right_region = [
    [
        # sg.Column([[sg.Text("Cantidad")], [sg.Text("Cantidad2")]]),
        sg.Column([[sg.Text(x)] for x in nota.cantidades]),
        sg.Column([[sg.Text(x)] for x in nota.descripciones]),
        sg.Column([[sg.Text(x)] for x in nota.pUnitarios]),
        sg.Column([[sg.Text(x)] for x in nota.importes])
     ]
 ]
layout = [
    title_region,
    [
        sg.Column(left_region),
        sg.VerticalSeparator(),
        sg.Column(right_region,key="cantidades", scrollable= True, size=(400,400))
        # sg.Column(genColumnObjs(nota.cantidades, 14),key="cDer", scrollable= True, size=(400,400))
     ],
    bottom_region
 ]


# Create the windows
main_window = sg.Window('Nota de venta', layout, background_color=BACKGROUND)

# Display and interact with the Window using an Event Loop
while True:
    event, values = main_window.read()
    if event == 'compra':
        print('Quiero registrar una compra!!')
        print(f"Cantidad: {values['cantidad']}\tDescripcion: {values['descripcion']}\tPrecio: {values['pUnit']}")
        nota.registrarVenta(int(values['cantidad']), values['descripcion'], int(values['pUnit']))

    elif event == 'print':
        # print(type(nota))
        # print(dir(nota))
        right_region = nota.getCantidades()
        main_window['cDer'].update(right_region)
        # main_window['strNota'].update(nota.__str__())
        print(nota)

    # See if window was closed
    elif event == sg.WINDOW_CLOSED:
        # print(nota)
        break

# Finish up by removing from the screen
main_window.close()
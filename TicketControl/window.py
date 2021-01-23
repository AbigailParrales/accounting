import PySimpleGUI as sg

from Nota import Nota
import tools

nota = Nota()

# Main window
topRegion = [
    sg.Text("Capturar venta", text_color='forest green', 
     font=('Helvetica',36, 'bold'), background_color=tools.BACKGROUND)
 ]
bottomRegion = [
    sg.Button('Vista previa de nota', key='genNota', button_color=('black', 'forest green'))
 ]
midRegion = [
    [sg.Text("Cantidad", size=(15, 1)), sg.Input(key='cantidad', do_not_clear = False)],
    [sg.Text("Descripcion", size=(15, 1)), sg.Input(key='descripcion', do_not_clear = False)],
    [sg.Text("Precio unitario", size=(15, 1)), sg.Input(key='pUnit', do_not_clear = False)],
    [sg.Button('Registrar compra', key='compra', button_color=('black', 'forest green'))]
 ]

layout = [
    topRegion,
    [sg.Column(midRegion)],
    # [
    #     sg.Column(left_region),
    #     sg.VerticalSeparator(),
    #     sg.Column(right_region,key="table", scrollable= True, size=(400,400))
    #  ],
    bottomRegion
 ]


# Create the windows
main_window = sg.Window('Generador de notas', layout, background_color=tools.BACKGROUND)

# Display and interact with the Window using an Event Loop
while True:
    event, values = main_window.read()
    if event == 'compra':
        print('Quiero registrar una compra!!')
        print(f"Cantidad: {values['cantidad']}\tDescripcion: {values['descripcion']}\tPrecio: {values['pUnit']}")
        nota.registrarVenta(int(values['cantidad']), values['descripcion'], int(values['pUnit']))

    elif event == 'genNota':
        nota_window = tools.makeNota(nota)
        event1, values1 = nota_window.read()
        print(nota)

    # See if window was closed
    elif event == sg.WINDOW_CLOSED:
        break

# Finish up by removing from the screen
main_window.close()
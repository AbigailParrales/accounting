import PySimpleGUI as sg

BACKGROUND = 'light yellow'

# Main window
title_region = [
    sg.Text("Nota de venta", text_color='forest green', 
     font=('Helvetica',36, 'bold'), background_color=BACKGROUND)
]
bottom_region = [
    sg.Button('Imprimir', key='print', button_color=('black', 'forest green'))
]
left_region = [
    [sg.Text("Cantidad"), sg.Input(key='cantidad')],
    [sg.Text("Descripcion"), sg.Input(key='descripcion')],
    [sg.Text("Precio unitario"), sg.Input(key='pUnit')],
    [sg.Button('Registrar compra', key='compra', button_color=('black', 'forest green'))]
]
right_region = [
    [sg.T('This is some random text')]
]
layout = [
    title_region,
    [sg.Column(left_region),sg.Column(right_region)],
    bottom_region
]



# Create the windows
main_window = sg.Window('Nota de venta', layout, background_color=BACKGROUND)

# Display and interact with the Window using an Event Loop
while True:
    event, values = main_window.read()
    if event == 'compra':
        print('quiero registrar una compra!!')
    # See if window was closed
    if event == sg.WINDOW_CLOSED:
        break

# Finish up by removing from the screen
main_window.close()
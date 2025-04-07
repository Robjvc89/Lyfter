import PySimpleGUI as sg
import json
import os

# Archivo de almacenamiento
ARCHIVO = 'finanzas.json'

# Estructura en memoria
datos = {
    "categorias": [],
    "movimientos": []
}

# Función para cargar los datos desde el archivo
def cargar_datos():
    global datos
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r') as file:
            datos = json.load(file)

# Función para guardar los datos en el archivo
def guardar_datos():
    with open(ARCHIVO, 'w') as file:
        json.dump(datos, file)

# Función para agregar una categoría
def agregar_categoria(nombre):
    if nombre not in datos['categorias']:
        datos['categorias'].append(nombre)
        guardar_datos()

# Función para agregar un movimiento (gasto o ingreso)
def agregar_movimiento(tipo, titulo, monto, categoria):
    movimiento = {"tipo": tipo, "titulo": titulo, "monto": monto, "categoria": categoria}
    datos['movimientos'].append(movimiento)
    guardar_datos()

# Crear ventana para agregar una categoría
def mostrar_ventana_categoria():
    layout = [
        [sg.Text('Agregar Nueva Categoría')],
        [sg.InputText(key='categoria')],
        [sg.Button('Agregar'), sg.Button('Cancelar')]
    ]
    ventana = sg.Window('Agregar Categoría', layout)
    
    while True:
        event, values = ventana.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Agregar':
            categoria = values['categoria']
            if categoria:
                agregar_categoria(categoria)
                sg.popup('Categoría agregada con éxito.')
            else:
                sg.popup_error('Por favor ingrese un nombre para la categoría.')
            break
    ventana.close()

# Crear ventana para agregar un gasto
def mostrar_ventana_gasto():
    if not datos['categorias']:
        sg.popup_error('Por favor ingrese una categoría antes de agregar un gasto.')
        return
    
    categorias = datos['categorias']
    layout = [
        [sg.Text('Agregar Gasto')],
        [sg.InputText('Título', key='titulo')],
        [sg.InputText('Monto', key='monto')],
        [sg.Combo(categorias, key='categoria', readonly=True)],
        [sg.Button('Agregar Gasto'), sg.Button('Cancelar')]
    ]
    ventana = sg.Window('Agregar Gasto', layout)
    
    while True:
        event, values = ventana.read()
        if event in (sg.WINDOW_CLOSED, 'Cancelar'):
            break
        if event == 'Agregar Gasto':
            titulo = values['titulo']
            monto = values['monto']
            categoria = values['categoria']
            if titulo and monto and categoria:
                agregar_movimiento('gasto', titulo, float(monto), categoria)
                sg.popup('Gasto agregado con éxito.')
            else:
                sg.popup_error('Por favor complete todos los campos.')
            break
    ventana.close()

# Crear ventana para agregar un ingreso
def mostrar_ventana_ingreso():
    if not datos['categorias']:
        sg.popup_error('Por favor ingrese una categoría antes de agregar un ingreso.')
        return
    
    categorias = datos['categorias']
    layout = [
        [sg.Text('Agregar Ingreso')],
        [sg.InputText('Título', key='titulo')],
        [sg.InputText('Monto', key='monto')],
        [sg.Combo(categorias, key='categoria', readonly=True)],
        [sg.Button('Agregar Ingreso'), sg.Button('Cancelar')]
    ]
    ventana = sg.Window('Agregar Ingreso', layout)
    
    while True:
        event, values = ventana.read()
        if event in (sg.WINDOW_CLOSED, 'Cancelar'):
            break
        if event == 'Agregar Ingreso':
            titulo = values['titulo']
            monto = values['monto']
            categoria = values['categoria']
            if titulo and monto and categoria:
                agregar_movimiento('ingreso', titulo, float(monto), categoria)
                sg.popup('Ingreso agregado con éxito.')
            else:
                sg.popup_error('Por favor complete todos los campos.')
            break
    ventana.close()

# Crear ventana principal con la tabla
def mostrar_ventana_principal():
    cargar_datos()  # Cargar los datos al inicio
    
    movimientos = [(mov['titulo'], mov['monto'], mov['categoria'], mov['tipo']) for mov in datos['movimientos']]
    
    layout = [
        [sg.Text('Gestión de Finanzas Personales')],
        [sg.Table(movimientos, headings=['Título', 'Monto', 'Categoría', 'Tipo'], key='tabla')],
        [sg.Button('Agregar Categoría'), sg.Button('Agregar Gasto'), sg.Button('Agregar Ingreso')]
    ]
    
    ventana = sg.Window('Gestión de Finanzas', layout)
    
    while True:
        event, values = ventana.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Agregar Categoría':
            mostrar_ventana_categoria()
        elif event == 'Agregar Gasto':
            mostrar_ventana_gasto()
        elif event == 'Agregar Ingreso':
            mostrar_ventana_ingreso()

    ventana.close()

if __name__ == '__main__':
    mostrar_ventana_principal()


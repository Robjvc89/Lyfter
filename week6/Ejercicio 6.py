def ordenar_palabras(string):
    
    
    lista_palabras = string.split('-')
    

    lista_palabras.sort()


    string_ordenado = '-'.join(lista_palabras)
    

    return string_ordenado


resultado = ordenar_palabras("python-variable-funcion-computadora-monitor")
print(resultado)  # Salida: "computadora-funcion-monitor-python-variable"

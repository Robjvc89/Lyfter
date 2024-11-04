def suma_lista(numeros):


    suma = 0  
    for numero in numeros:
        suma += numero 
    return suma 


lista_numeros = [15, 22, 34, 14, 5]
resultado = suma_lista(lista_numeros)
print("La suma de los números en la lista es:", resultado)

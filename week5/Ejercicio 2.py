texto = input("Ingrese un texto:")

longitud = len(texto)  # Obtener la longitud del string
for i in range(longitud - 1, -1, -1):  # Iterar desde el último índice hasta el primero
        print(texto[i])  # Imprimir cada letra

# Ejemplo de uso


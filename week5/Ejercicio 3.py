entrada = input("Ingrese los elementos de la lista separados por comas:")

lista = entrada.split(",")

# Comprobar si la lista tiene al menos 2 elementos
if len(lista) < 2:
    print("La lista debe tener al menos dos elementos para intercambiar.")
else:
    # Intercambiar el primer y último elemento
    lista[0], lista[-1] = lista[-1], lista[0]

# Imprimir la lista modificada
print(lista)

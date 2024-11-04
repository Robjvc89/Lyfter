entrada = input("Ingresa los numeros separados por comas:")

lista = [int(num) for num in entrada.split(",")]

lista_pares = [num for num in lista if num % 2 == 0]

print("Lista despues de eliminar los numero impares:",lista_pares)

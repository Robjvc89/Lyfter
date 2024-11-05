numeros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: ")) 
    numeros.append(numero)

numero_mas_alto = max(numeros)

print("Números ingresados:", numeros)
print("Número más alto:", numero_mas_alto)

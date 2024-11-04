import random

# Generar un número secreto del 1 al 10
numero_secreto = random.randint(1, 10)

print("Bienvenido al juego de adivinar el número.")
print("He elegido un número entre 1 y 10. ¡Intenta adivinarlo!")

# Bucle para solicitar adivinanzas
while True:
    # Solicitar al usuario que ingrese su adivinanza
    try:
        adivinanza = int(input("Introduce tu adivinanza: "))
        
        # Verificar la adivinanza
        if adivinanza < 1 or adivinanza > 10:
            print("Por favor, elige un número entre 1 y 10.")
        elif adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print("¡Felicidades! Adivinaste el número.")
            break  # Salir del bucle si adivina correctamente

    except ValueError:
        print("Por favor, ingresa un número válido.")

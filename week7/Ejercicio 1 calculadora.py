def mostrar_menu ():
    print("\nSelecciona una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar Resultado")
    print("6. Salir")


def obtener_numero():
    while True:
        try:
            num = float(input("Ingresa un numero"))
            return num
        except ValueError:
            print("Error: Debes ingresar un codigo valido.")


def main():
    numero_actual = 0.0
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-6):")

        if opcion == '1':
            nuevo_numero = obtener_numero()
            numero_actual += nuevo_numero
            print(f"Numero actual despues de la suma: {numero_actual}")

        elif opcion == '2':
            nuevo_numero = obtener_numero()
            numero_actual -= nuevo_numero
            print(f"Numero actual despues de la resta: {numero_actual}")

        elif opcion == '3':
            nuevo_numero = obtener_numero()
            numero_actual *= nuevo_numero
            print(f"Numero actual despues de la multiplicacion: {numero_actual}")

        elif opcion == '4':
            nuevo_numero = obtener_numero()
            try:
                if nuevo_numero == 0:
                    raise ZeroDivisionError
                numero_actual /= nuevo_numero
                print(f"Numero actual despues de la division: {numero_actual}")
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero.")
            
        elif opcion == '5':
            numero_actual = 0.0
            print("Numero actual ha sido borrado. Numero actual: 0.0")

        elif opcion == '6':
            print("Saliendo de la calculadora. ¡Hasta pronto!")
            break 

        else:
            print("Error: Opcion invalida. Por favor selecciona una opcion entre 1 y 6.")


if __name__ == "__main__":
    main()

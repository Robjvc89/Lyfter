def contar_mayusculas_minusculas(cadena):
    
    
    conteo_mayusculas = 0
    conteo_minusculas = 0


    for caracter in cadena:
        if caracter.isupper():  # Verifica si el carácter es mayúscula
            conteo_mayusculas += 1
        elif caracter.islower():  # Verifica si el carácter es minúscula
            conteo_minusculas += 1

    print(f"There’s {conteo_mayusculas} upper cases and {conteo_minusculas} lower cases.")

# Ejemplo de uso
texto = "Vamos a visitar Medio Oriente."
contar_mayusculas_minusculas(texto)

def ingresar_videojuegos():
    n = int(input("¿Cuántos videojuegos desea ingresar? "))
    videojuegos = []

    for _ in range(n):
        nombre = input("Ingrese el nombre del videojuego: ")
        genero = input("Ingrese el género del videojuego: ")
        desarrollador = input("Ingrese el desarrollador del videojuego: ")
        clasificacion = input("Ingrese la clasificación ESRB del videojuego: ")
        
        videojuego = {
            'nombre': nombre,
            'genero': genero,
            'desarrollador': desarrollador,
            'clasificacion': clasificacion
        }
        videojuegos.append(videojuego)

    return videojuegos

def guardar_en_txt(videojuegos, archivo):
    with open(archivo, 'w', encoding='utf-8') as txtfile:
        # Escribir la cabecera
        txtfile.write('nombre\tgenero\tdesarrollador\tclasificacion\n')
        # Escribir los datos de cada videojuego
        for videojuego in videojuegos:
            txtfile.write(f"{videojuego['nombre']}\t{videojuego['genero']}\t{videojuego['desarrollador']}\t{videojuego['clasificacion']}\n")

def main():
    videojuegos = ingresar_videojuegos()
    archivo_txt = 'videojuegos.tsv'  # Usamos .tsv para indicar que es un archivo separado por tabulaciones
    guardar_en_txt(videojuegos, archivo_txt)
    print(f"\nLa información de los videojuegos ha sido guardada en {archivo_txt}.")

if __name__ == "__main__":
    main()

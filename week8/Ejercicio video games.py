import csv

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

def guardar_en_csv(videojuegos, archivo):
    with open(archivo, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['nombre', 'genero', 'desarrollador', 'clasificacion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Escribir los nombres de las columnas
        for videojuego in videojuegos:
            writer.writerow(videojuego)

def main():
    videojuegos = ingresar_videojuegos()
    archivo_csv = 'videojuegos.csv'
    guardar_en_csv(videojuegos, archivo_csv)
    print(f"\nLa información de los videojuegos ha sido guardada en {archivo_csv}.")

if __name__ == "__main__":
    main()

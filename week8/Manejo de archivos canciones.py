def open_and_print_file_per_line(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            canciones = [line.strip() for line in file]  # Leer y limpiar las líneas

        # Imprimir las canciones
        for cancion in canciones:
            print(f'Canción: {cancion}')
        
        # Ordenar las canciones alfabéticamente
        canciones.sort()

        # Guardar las canciones ordenadas en otro archivo
        with open(output_path, 'w', encoding='utf-8') as file:
            for cancion in canciones:
                file.write(cancion + '\n')  

        print(f'\nLas canciones han sido guardadas en {output_path} ordenadas alfabéticamente.')

    except FileNotFoundError:
        print(f'El archivo {input_path} no se encontró.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')


input_file = 'canciones.txt'  
output_file = 'canciones_ordenadas.txt' 

open_and_print_file_per_line(input_file, output_file)


import json
import os

def cargar_pokemons(archivo):
    if not os.path.exists(archivo):
        return []
    with open(archivo, 'r') as f:
        return json.load(f)

def guardar_pokemons(archivo, pokemons):
    with open(archivo, 'w') as f:
        json.dump(pokemons, f, indent=2)

def agregar_pokemon(archivo):
    pokemons = cargar_pokemons(archivo)

    nombre = input("Ingrese el nombre del Pokemon: ")
    tipo = input("Ingrese el tipo del Pokemon (separado por comas si tiene mas de uno): ").split(',')
    tipo = [t.strip() for t in tipo]
    
    base = {
        "HP": int(input("Ingrese los HP: ")),
        "Attack": int(input("Ingrese el Ataque: ")),
        "Defense": int(input("Ingrese la Defensa: ")),
        "Sp. Attack": int(input("Ingrese el Ataque Especial: ")),
        "Sp. Defense": int(input("Ingrese la Defensa Especial: ")),
        "Speed": int(input("Ingrese la Velocidad: "))
    }

    nuevo_pokemon = {
        "name": {"english": nombre},
        "type": tipo,
        "base": base
    }

    pokemons.append(nuevo_pokemon)
    guardar_pokemons(archivo, pokemons)
    print(f"{nombre} ha sido agregado exitosamente.")

if __name__ == "__main__":
    archivo_pokemons = 'pokemons.json'
    agregar_pokemon(archivo_pokemons)

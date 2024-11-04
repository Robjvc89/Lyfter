# Solicitar al usuario la cantidad de notas
n = int(input("Ingrese la cantidad de notas: "))

# Inicializar listas y contadores
notas = []
aprobadas = []
desaprobadas = []

# Recoger las notas del usuario
for i in range(n):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)
    if nota >= 70:
        aprobadas.append(nota)
    else:
        desaprobadas.append(nota)

# Calcular resultados
cantidad_aprobadas = len(aprobadas)
cantidad_desaprobadas = len(desaprobadas)
promedio_total = sum(notas) / n if n > 0 else 0
promedio_aprobadas = sum(aprobadas) / cantidad_aprobadas if cantidad_aprobadas > 0 else 0
promedio_desaprobadas = sum(desaprobadas) / cantidad_desaprobadas if cantidad_desaprobadas > 0 else 0

# Mostrar resultados
print(f"\nNotas aprobadas: {cantidad_aprobadas}")
print(f"Notas desaprobadas: {cantidad_desaprobadas}")
print(f"Promedio total: {promedio_total:.2f}")
print(f"Promedio de notas aprobadas: {promedio_aprobadas:.2f}")
print(f"Promedio de notas desaprobadas: {promedio_desaprobadas:.2f}")

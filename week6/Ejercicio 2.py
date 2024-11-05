# Variable global
contador_global = 0

def funcion_con_variable_local():
    # Variable local
    contador_local = 5
    print("Dentro de la funcion:")
    print("Valor de contador_local:", contador_local)

# Intentamos acceder a la variable local fuera de la función
try:
    funcion_con_variable_local()
    print("Fuera de la funcion:")
    print("Valor de contador_local:", contador_local) 
    
except NameError as e:
    print("Error:", e)  

def funcion_cambiar_global():
    global contador_global  
    contador_global += 1  # Cambiamos el valor de la variable global
    print("Dentro de la funcion para cambiar el global:")
    print("Valor de contador_global:", contador_global)


funcion_cambiar_global()

print("Fuera de la funcion:")
print("Valor de contador_global:", contador_global)

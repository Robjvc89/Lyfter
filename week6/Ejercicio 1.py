def funcion_secundaria():
    print("No podemos estar en modo de supervivencia.")

def funcion_principal():
    print("Tenemos que estar en modo de crecimiento.")
    funcion_secundaria()  


funcion_principal()

def es_primo(num):


    if num <= 1:
        return False
    

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  
            return False
    return True  


def filtrar_primos(lista):
    lista_primos = []  
    for numero in lista:  
        if es_primo(numero):  
            lista_primos.append(numero) 
    return lista_primos  


numeros = [1, 4, 6, 7, 13, 9, 67]
primos = filtrar_primos(numeros)
print(primos)  

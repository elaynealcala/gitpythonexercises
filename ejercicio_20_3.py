# Descripcion: Funcion que valida si un numero n se encuentra en una lista de numeros l
# Entrada: Un numero n y una lista de numeros l
# Salida:  Cierto o falso (cierto si el numero n pertenece a la lista l, falso en caso contrario)
# Autor:   EALCALA
# Fecha:  23.05.2017
# Version: 3.0
#Plataforma: Python v2.7

def fun_bool(n):
    import random
    l = []
    for i in range(0,100):
        l.append(random.randint(0,100))
    verd = n in l
    if verd:
        print("el numero esta en la lista")
    else:
        print("el numero no esta en la lista")

n = int(input("Ingrese un numero para comprobar si esta o no dentro de la lista: "))
fun_bool(n)

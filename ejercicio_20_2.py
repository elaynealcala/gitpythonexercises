# Descripcion: Funcion que valida si un numero n se encuentra en una lista de numeros l
# Entrada: Un numero n y una lista de numeros l
# Salida:  Cierto o falso (cierto si el numero n pertenece a la lista l, falso en caso contrario)
# Autor:   EALCALA
# Fecha:  23.05.2017
# Version: 2.0
#Plataforma: Python v2.7

def fun_bool(n):
    l = [1,2,3,4,5,6,7,8,9]
    verd = n in l
    if verd:
        print("el numero pertenece a la lista")
    else:
        print("el numero no esta en la lista")

n = 11
fun_bool(n)

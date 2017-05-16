# Descripcion: Programa que pregunta al usuario por cuantos numeros de la serie fibonacci desea generar y los da como salida, utilizando una funcion definida fibnum
# Entrada: Numero n de numeros de la serie Fibonacci a generar
# Salida:  n numeros de la serie Fibonacci
# Autor:   EALCALA
# Fecha:  12.05.2017
# Version: 1.0
#Plataforma: Python v2.7

def fibnum():
    n = input("Introduzca el numero de numeros de la serie Fibonacci que desea generar: ")
    if not n.isnumeric():
        raise Exception("Favor ingresar solamente numeros")
    n = int(n)
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)

fibnum()

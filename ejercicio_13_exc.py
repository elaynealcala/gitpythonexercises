# Descripcion: Programa que pregunta al usuario por cuantos numeros de la serie fibonacci desea generar y los da como salida, utilizando una funcion definida fibnum
# Entrada: Numero n de numeros de la serie Fibonacci a generar
# Salida:  n numeros de la serie Fibonacci
# Autor:   EALCALA
# Fecha:  12.05.2017
# Version: 1.0
#Plataforma: Python v2.7

def fibnum(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)
while True:
 try:
  n = int(raw_input("Introduzca el numero de numeros de la serie Fibonacci que desea generar: "))
  break
 except ValueError:
  print ("Usted no introdujo un numero! favor introduzca un numero entero: ")

fibnum(n)

# Descripcion: programa que regresa una frase al reves de como fue introducida por un usuario
# Entrada: Frase suministrada por el usuario
# Salida:  Frase invertida
# Autor:   EALCALA
# Fecha:  16.05.2017
# Version: 1.0
#Plataforma: Python v2.7

a = raw_input("Ingrese la frase que desea invertir: ")
def rev_str(a):
    b = a.split()
    b.reverse()
    return " ".join(b)

print rev_str(a)

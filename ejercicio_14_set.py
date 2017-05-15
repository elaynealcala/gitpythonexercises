# Descripcion: Programa que genera una lista aleatoriamente y regresa una lista con los elementos de la primera lista sin duplicados
# Entrada: Lista generada aleatoriamente por el programa
# Salida:  Lista de elementos de la lista generada sin duplicados
# Autor:   EALCALA
# Fecha:  15.05.2017
# Version: 1.0
#Plataforma: Python v2.7

import random
a = []
def no_dupl(a):
 for i in range(0,10):
  a.append(random.randint(0,100))
 return(list(set(a)))

print no_dupl(a)

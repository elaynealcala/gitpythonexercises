# Descripcion: Programa que genera una lista aleatoriamente y regresa una lista con los elementos de la primera lista sin duplicados
# Entrada: Lista generada aleatoriamente por el programa
# Salida:  Lista de elementos de la lista generada sin duplicados
# Autor:   EALCALA
# Fecha:  15.05.2017
# Version: 1.0
#Plataforma: Python v2.7

import random
a = []
b = []
def no_dupl(a,b):
 for i in range(0,100):
  a.append(random.randint(0,100))
 for i in a:
  if i not in b:
   b.append(i)
 return b

print no_dupl(a,b)

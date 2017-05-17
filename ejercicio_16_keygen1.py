# Descripcion: Programa que genera una contrasena fuerte
# Entrada: Solicitud de contrasena
# Salida:  Contrasena aleatoriamente generada
# Autor:   EALCALA
# Fecha:  17.05.2017
# Version: 1.0
#Plataforma: Python v2.7

def clave_gen(len=10): #defino una funcion
    import random #importo la libreria random, que genera items aleatoriamente
    items = "1234567890!@#$%*()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lista_items = list(items)
    return ''.join(random.sample(lista_items,len))
    return lista_items

print clave_gen()

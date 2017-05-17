# Descripcion: Programa que genera una contrasena fuerte o debil segun desea el usuario
# Entrada: Solicitud de contrasena fuerte o debil
# Salida:  Contrasena aleatoriamente generada
# Autor:   EALCALA
# Fecha:  17.05.2017
# Version: 3.0
#Plataforma: Python v2.7

def nivel():
    return raw_input("Introduzca un nivel de seguridad de contrasena:['debil' || 'fuerte'] :")

def clave_deb(len=5):
    import random
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lista_items = list(items)
    return ''.join(random.sample(lista_items,len))
    return lista_items

def clave_fuer(len=10):
    import random
    items = "1234567890!@#$%*()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lista_items = list(items)
    return ''.join(random.sample(lista_items,len))
    return lista_items

def clave():
    n = nivel()
    if (n.lower() == 'debil'):
        print "Contrasena : " ,clave_deb()
    elif (n.lower() == 'fuerte'):
        print "Contrasena : ", clave_fuer()
    else:
        print "Usted no introdujo una opcion, valida"

clave()

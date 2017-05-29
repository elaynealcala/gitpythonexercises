# Descripcion: Programa que permite a un usuario jugar a Piedra, papel o tijera con un jugador virtual PC
# Entrada: Seleccion entre piedra, papel o tijera hecha por el usuario
# Salida:  Felicitaciones al usuario ganador
# Autor:   EALCALA
# Fecha:  03.05.2017
# Version: 1.0
#Plataforma: Python v2.7

import sys
w = int(input("Escribe 3 si deseas jugar piedra, papel o tijera, o 4 si no deseas jugar: "))
if w == 4:
    sys.exit("Adios")
while w == 3:
    import random
    a = random.randrange(0, 3)
    Pc = ""
    print("Escoge 0)Piedra")
    print("1)Papel")
    print("2)Tijera")
    j1 = int(input("Escoge una opcion: "))

    if j1 == 0:
        Usuario = "piedra"
    elif j1 == 1:
        Usuario = "papel"
    elif j1 == 2:
        Usuario = "tijera"

    if a == 0:
        Pc = "piedra"
    elif a == 1:
        Pc = "papel"
    elif a == 2:
        Pc = "tijera"

    print("...")
    if Pc == "piedra" and Usuario == "papel":
        print("Ganaste!!, papel gana a piedra")
    elif Pc == "papel" and Usuario == "tijera":
        print("Ganaste!!, Tijera gana a papel")
    elif Pc == "tijera" and Usuario == "piedra":
        print("Ganaste!!, Piedra gana a tijera")
    elif Pc == "papel" and Usuario == "piedra":
        print("Perdiste!!, papel gana a piedra")
    elif Pc == "tijera" and Usuario == "papel":
        print("perdiste!!, Tijera gana a papel")
    elif Pc == "piedra" and Usuario == "tijera":
        print("perdiste!!, Piedra gana a tijera")
    elif Pc == Usuario:
        print("Hay un empate")
    break

sys.exit()

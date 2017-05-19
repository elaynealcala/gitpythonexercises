# Descripcion: Programa que juega con un usuario vacas y toros
# Entrada: Eleccion para adivinar de un numero de 4 digitos
# Salida:  Numero de Vacas y Toros hasta acertar
# Autor:   EALCALA
# Fecha:  19.05.2017
# Version: 1.0
#Plataforma: Python v2.7

def vacas_toros():

    from random import randint
    vacas = 0
    toros = 0
    uno = randint(1,9)
    dos = randint(1,9)
    tres = randint(1,9)
    cuatro = randint(1,9)
    num = str(uno) + str(dos) + str(tres) + str(cuatro)
    while True:
        vacas = toros = 0
        adiv = input('Bienvenido al juego de vacas y toros, adivine un numero de cuatro digitos: ')
        for i in adiv:
            if i in num:
                vacas += 1
            else:
                toros += 1
        if toros == 0:
            print('Usted ha adivinado el numero')
            break
        else:
            print('Llevas ' + str(cows) + ' vacas, y ' + str(bulls) + ' toros!')
            continue

if __name__=="__main__":
    vacas_toros()

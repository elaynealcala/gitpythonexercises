# Descripcion: Programa que lee un archivo .txt
# Entrada: Archivo .txt
# Salida: Archivo .txt con las noticias de la web New York Times
# Autor:   EALCALA
# Fecha:  24.05.2017
# Version: 1.0
#Plataforma: Python v2.7


print("Favor descargar archivo nombres.txt en el mismo directorio en donde se ejecutara el programa")
with open("nombres.txt", "r") as nombres:
    num_nombres = dict()
    for i in nombres:
        if i.replace("\n", "") in num_nombres.keys():
            num_nombres[i.replace("\n", "")] += 1
        else:
            num_nombres[i.replace("\n", "")] = 1

    print(num_nombres)

print(2*"\n")

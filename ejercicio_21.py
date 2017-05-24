# Descripcion: Programa que extrae el contenido de una pagina web y lo envia a un archivo de texto cuyo nombre da el usuario
# Entrada: Nombre del archivo .txt
# Salida: Archivo .txt con las noticias de la web New York Times
# Autor:   EALCALA
# Fecha:  24.05.2017
# Version: 1.0
#Plataforma: Python v2.7

arch_nom = raw_input("Escoja un nombre para la salida de los titulares de la web The New York Times: ") #invita al usuario a escoger un nombre

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.nytimes.com')
s = BeautifulSoup(r.text)

with open(arch_nom, 'w') as arch:
    for titulares in s.find_all(class_="story-heading"):
        if titulares.a:
            arch.write(titulares.a.text.replace("\n", " ").strip())
        else:
            arch.write(titulares.contents[0].strip())

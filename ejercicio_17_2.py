# Descripcion: Programa que decodifica la pagina web de The Newe York Times
# Entrada: Pagina web The New York Times
# Salida:  Lista de titulos de los articulos en la web
# Autor:   EALCALA
# Fecha:  18.05.2017
# Version: 2.0
#Plataforma: Python v2.7

import requests
from bs4 import BeautifulSoup
web = 'http://nytimes.com'
lista = []
req_web = requests.get(web)
ext_dat = BeautifulSoup(req_web.text, "lxml")
noticias = ext_dat.find_all(class_="story-heading")
for i in noticias:
    lista.append(i)

print (lista)

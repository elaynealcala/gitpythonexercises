# Descripcion: Programa que decodifica la pagina web de The Newe York Times
# Entrada: Pagina web The New York Times
# Salida:  Titulos de los articulos en la web
# Autor:   EALCALA
# Fecha:  18.05.2017
# Version: 1.0
#Plataforma: Python v2.7

import requests
from bs4 import BeautifulSoup
web = 'http://nytimes.com'
req_web = requests.get(web)
ext_dat = BeautifulSoup(req_web.text, "lxml")
noticias = ext_dat.find_all(class_="story-heading")
print (noticias)

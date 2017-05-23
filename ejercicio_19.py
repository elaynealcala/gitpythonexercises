# Descripcion: Programa que decodifica el contenido de una pagina web, imprimiendo como salida el contenido del articulo disponible en una pagina precargada
# Entrada: Pagina web  http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
# Salida:  Articulo completo en una sola pagina
# Autor:   EALCALA
# Fecha:  22.05.2017
# Version: 1.0
#Plataforma: Python v2.7

import requests
from bs4 import BeautifulSoup
web = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
art = requests.get(web)
Bs = BeautifulSoup(art.text, "lxml")
data = Bs.find_all(class_="content-section")
for i in data:
    print i

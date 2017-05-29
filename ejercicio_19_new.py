# Descripcion: Programa que decodifica el contenido de una pagina web, imprimiendo como salida el contenido del articulo disponible en una pagina precargada
# Entrada: Pagina web  http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
# Salida:  Articulo completo en una sola pagina
# Autor:   EALCALA
# Fecha:  22.05.2017
# Version: 1.0
#Plataforma: Python v2.7

print("Bienvenido, favor recuerde instalar la libreria BeautifulSoup4")
import requests
from bs4 import BeautifulSoup
web = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
art = requests.get(web)
l1 = BeautifulSoup(art.content, "html.parser")
l2 = l1.find_all('div', {"class:" "dek"})
for i in l2:
    print(i.text)
l3 = l1.find_all('section', {"class:", "content-section"})
for i in l3:
    print(i.text)

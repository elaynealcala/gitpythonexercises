# Descripcion: Programa que decodifica la pagina web de The New York Times
# Entrada: Pagina web The New York Times
# Salida:  Titulos de los articulos en la web
# Autor:   EALCALA
# Fecha:  18.05.2017
# Version: 1.0
#Plataforma: Python v2.7

print("Bienvenido, favor recuerde instalar la libreria BeautifulSoup4")
import requests
from bs4 import BeautifulSoup
web = 'http://nytimes.com'
req_web = requests.get(web)
ext_dat = BeautifulSoup(req_web.text, "lxml")

for articulo in ext_dat.find_all(class_="story-heading"):
 if articulo.a:
  print(articulo.a.text.replace("\n", " ").strip())
 else:
  print(articulo.contents[0].strip())

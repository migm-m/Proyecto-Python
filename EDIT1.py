#EDIT NAY LEER LINEAS


# IMPORTAR MÓDULOS PARA TRABAJAR
import requests
from bs4 import BeautifulSoup
from io import open
import pandas as pd


#Pedir el archivo donde se tiene los links
instex = input('Inserte el nombre de su archivo txt (Ejemplo: fuentes.txt)')

lista = []

# abrir el archivo de texto que tiene los links de donde se obtiene la información
archivo = open(instex, "r", encoding="utf-8")
links = archivo.readlines()



# creación de una variable para almacenar la información
for i in range (len(links)):
    url = links[i]
    response = requests.get(url)

    # selección de html de donde de se obtendra la info del sitio web
    soup = BeautifulSoup(response.text, 'html.parser')
  #el problema recae aqui, quiza otro for verificando que todo este ahi y si no que pase, pero la verdad no se.
    headlines = soup.find('body').find_all('h2')
    tit = soup.find('head').find('title').text
    y = 1
    print("Fuente: "+tit)


    for x in headlines:
      print("Titular " + str(y), ": ", x.text.strip())
      y = y + 1


archivo.close()
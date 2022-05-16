#IMPORTAR MÓDULOS PARA TRABAJAR
import requests
from bs4 import BeautifulSoup
from io import open

#abrir el archivo de texto que tiene los links de donde se obtiene la información
def getheads():
  #abrir el archivo de texto que tiene los links de donde se obtiene la información
  archivo=open(r"text.txt", "r", encoding = "utf-8")
  links=archivo.read()
  
  
  #creación de una variable para almacenar la información
  url=links
  response = requests.get(url)
  
  #selección de html de donde de se obtendra la info del sitio web
  soup = BeautifulSoup(response.text, 'html.parser')
  headlines = soup.find('body').find_all('h2')
  y = 1
  heads=list()
  print ("Fuente: Milenio")
  for x in headlines:
      heads.append("Titular "+ str(y)+ ": "+ x.text.strip())
      y = y + 1
  
  archivo.close()
  return heads
  #input()

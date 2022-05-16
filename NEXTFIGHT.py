#IMPORTAR MÓDULOS PARA TRABAJAR
import requests
from bs4 import BeautifulSoup
from io import open

def getnext():
  #abrir el archivo de texto que tiene los links de donde se obtiene la información
  archivo=open(r"next.txt", "r", encoding = "utf-8")
  links=archivo.read()
  
  
  #creación de una variable para almacenar la información
  url=links
  response = requests.get(url)
  
  #selección de html de donde de se obtendra la info del sitio web
  soup = BeautifulSoup(response.text, 'html.parser')
  headlines = soup.find('body').find_all('h1')
  prox=list()
  for x in headlines:
      prox.append(x.text.strip())

  archivo.close()
  return prox
  #input()

#IMPORTAR MÓDULOS PARA TRABAJAR
import requests
from bs4 import BeautifulSoup
from io import open

def getinfo():
  #abrir el archivo de texto que tiene los links de donde se obtiene la información
  archivo=open(r"info.txt", "r", encoding = "utf-8")
  links=archivo.read()
  
  
  #creación de una variable para almacenar la información
  url=links
  response = requests.get(url)
  
  #selección de html de donde de se obtendra la info del sitio web
  soup = BeautifulSoup(response.text, 'html.parser')
  headlines = soup.find('ul').find_all('li')
  print ("Canelo Alvarez")
  print ("Age, Height, Weight Class, Reach, Titles")
  inf=list()
  for x in headlines:
      inf.append(x.text.strip())
  
  archivo.close()
  return inf

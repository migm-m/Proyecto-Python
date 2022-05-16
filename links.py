import requests
from io import open
import re

def getlinks():
 # impresión de archivo antes de modificarse
  with open(r"fuentes.txt", "r", encoding = "utf-8") as archivo:
    urls=list()
    lineas = archivo.readlines()
    for i in lineas:
      urls.append(i.strip("\n"))        
    for i in urls:
      links = requests.get(i)
      
  return urls

def intolink(nlink):
  # abrir el archivo a editar, pedir input del url y cerrar archivo
  archivo = open(r"fuentes.txt", "a", encoding = "utf-8")  # "a" para agregar al final del txt (append)
  archivo.write(nlink)
  archivo.close()
  
     
  # volver a abrir el archivo para imprimir en pantalla el nuevo contenido del txt
  """archivo = open(r"fuentes.txt", "r", encoding = "utf-8")
  print("El contenido del archivo de texto actualizado: ")
  print(archivo.read())
  print()
  
  # cerrar archivo para guardar cambios
  archivo.close()
  
  return text"""
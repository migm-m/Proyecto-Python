import requests 

def clima():
  ciudad = input("Ingresa la ciudad a investigar: ")
  
  url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=25d896c3a747fe3d28d65e07207a3f04&units=metric".format(ciudad)
  
  lugar= requests.get(url)
  
  datos = lugar.json()
  
  temperaturamin = datos["main"]["temp_min"]
  temperaturamax = datos["main"]["temp_max"] 
  
  latitud = datos["coord"]["lat"]
  longitud = datos["coord"]["lon"]
  
  descripcion = datos["weather"][0]["description"]
  
  
  print("La temperatura minima es: ", temperaturamin)
  print("La temperatura maxima es: ", temperaturamax)
  print("Descripcion: ", descripcion)

from tkinter import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup

from stats import getstats
from HEADLINES import getheads
from INFO import getinfo
from links import *
from NEXTFIGHT import getnext

info = StringVar

inicio = Tk()
inicio.title("prueba")
inicio.geometry("710x550")
inicio.config(bg="#200129255")

fr1 = Frame(inicio, width=710, height=180)
fr1.pack(fill="x", expand="true")
fr1.config(bg="#255000000")
fr1.place(x=0, y=0)

fr2 = Frame(inicio, width=710, height=340)
fr2.pack(fill="x", expand="true")
fr2.place(x=0, y=180)
fr2.config(bg="#182000017")

fr3=Frame(inicio, width=705, height=450)
fr3.place(x=0, y=240)
fr3.config(bg="#182000017")

def clear():
  list = fr2.winfo_children()
  for l in list:
    l.destroy()
  clear2()
  
def clear2():
  list2 = fr3.winfo_children()
  for li in list2:
    li.destroy()

def historia():
  clear()
  info = "Sobre el"
  lb3 = Label(fr2, text=info)
  lb3.pack()
  lb3.place(x=10, y=10)
  inf=list()
  i=list()
  inf=getinfo()
  a=0
  for x in inf:     
    i=Label(fr3, text=x)
    i.pack()
    i.place(x=10, y=a)
    a=a+20
  return info

def peleas():
  clear()
  info = "peleas de canelo"
  lb3 = Label(fr2, width=13, height=1, text=info)
  lb3.pack()
  lb3.place(x=10, y=10)
  bt6=Button(fr2, width=15, height=1, text="Stats de sus peleas", command=stats)
  bt6.place(x=10, y=30)
  bt7=Button(fr2, width=15, height=1, text="Su proxima pelea", command=next)
  bt7.place(x=165, y=30)
  
  return info


def noti():
  clear()
  info = "Noticias"
  lb3 = Label(fr2, text=info)
  lb3.pack()
  lb3.place(x=10, y=10)
  notis=list()
  n=list()
  notis = getheads()
  a=0
  for x in notis:     
    n=Label(fr3, text=x)
    n.pack()
    n.place(x=10, y=a)
    a=a+20
  return info

def fotos():
  clear()
  info = "fotos"
  lb3 = Label(fr2, text=info)
  lb3.pack()
  lb3.place(x=10, y=10)
  return info

def mas():
  clear()
  info = "Mas información en: "
  lb3 = Label(fr2, text=info)
  lb3.pack()
  lb3.place(x=10, y=10)
  lin=list()
  l=list()
  lin = getlinks()
  a=0
  for x in lin:     
    l=Label(fr3, text=x)
    l.pack()
    l.place(x=10, y=a)
    a=a+20

  lb5=Label(fr3, text="tines mas información? escribe aquí el link")
  lb5.pack()
  lb5.place(x=10, y=a+30)
  txt1=Entry(fr3)
  txt1.pack()
  txt1.place(x=270, y=a+29)
  bt7=Button(fr3, text="agregar link", command=newlink)  
  bt7.pack()
  bt7.place(x=435, y=a+26)
  return info
def newlink():
  nlink=txt1.get()
  intolink(nlink)
def stats():
  clear2()  
  info=getstats()
  lb4=Label(fr3, justify="left", text=info.draw())
  lb4.pack()
  lb4.place(x=0, y=9)
  return info

def next():
  clear2()
  
  prx=list()
  p=list()
  prx = getnext()
  a=2
  for x in prx:     
    p=Label(fr3, text=x)
    p.pack()
    p.place(x=10, y=a)
    a=a+20
  return info

img1=Image.open("ini.png")
img1r=img1.resize((110,120))
im1=ImageTk.PhotoImage(img1r)
fot1=Label(fr1, image=im1).place(x=245, y=5)
lb1 = Label(fr1, width=12, height=1, text="Canelo Alvarez")
lb1.pack()
lb1.place(x=250, y=120)
bt1 = Button(fr1, width=11, height=1, text="Sobre el", command=historia)
bt1.place(x=5, y=140)
bt2 = Button(fr1, width=11, height=1, text="Sus peleas", command=peleas)
bt2.place(x=125, y=140)
bt3 = Button(fr1, width=11, height=1, text="Noticias", command=noti)
bt3.place(x=245, y=140)
bt4 = Button(fr1, width=11, height=1, text="Galeria de fotos", command=fotos)
bt4.place(x=365, y=140)
bt5 = Button(fr1, width=11, height=1, text="Mas Info", command=mas)
bt5.place(x=485, y=140)

inicio.mainloop()

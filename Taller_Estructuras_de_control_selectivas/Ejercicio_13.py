from datetime import datetime
from tkinter import E

hoy=datetime.now()
diaA=hoy.day
mesA=hoy.month
anioA=hoy.year
#Entrada
fecha=input("Poner en formato dd/mm/yyyy")
(dia,mes,anio)=fecha.split("/")
diaN= int (dia)
mesN= int (mes)
anioN= int (anio)
#Caja negra
Edad=0
if mesA>mesN:
    Edad= int (anioA-anioN)
elif mesA<mesN:
    Edad= int(anioA-anioN)-1
elif mesA==mesN:
    if diaA<diaN:
        Edad= int(anioA-anioN)-1
    elif diaA>diaN:
        Edad= int (anioA-anioN)
    elif diaA==diaN:
        Edad= int (anioA-anioN)
signo=""
if mes==1:
    signo="Acuario"
elif mes==2:
    signo="Piscis"
elif mes==3:
    signo="Piscis"
elif mes==4:
    signo="Piscis"
elif mes==5:
    signo="Piscis"
elif mes==6:
    signo="Piscis"
elif mes==7:
    signo="Piscis"
elif mes==8:
    signo="Piscis"
elif mes==9:
    signo="Piscis"
elif mes==10:
    signo="Piscis"
elif mes==11:
    signo="Piscis"
elif mes==12:
    signo="Piscis"
#Salida
print("Edad", Edad, "signo", signo)

#Entradas
from calendar import c
from pickle import TRUE


c1= float (input("Primera calificación parcial: "))
c2= float (input("Segunda calificación parcial: "))
c3= float (input("Tercera calificación parcial: "))
cE= float (input("Calificación examen final: "))
cT= float (input("Calificación del trabajo final: "))
#Caja negra
cT= float ((c1+c2+c3)/3)*0.55
cET=cE*0.30
cTF=cT*0.15
cF=cT+cET+cTF
cF=round(cF,2)
#Salidas
print ("La calificación final del alumno es de:", cF)
#Entrada
categoria=int(input())
sueldo= int(input())
#Caja negra 
aumento=0
if categoria==1:
    aumento=sueldo+sueldo*0.1
elif categoria==2:
    aumento=sueldo+sueldo*0.15
elif categoria==3:
    aumento=sueldo+sueldo*0.20
elif categoria==4:
    aumento=sueldo+sueldo*0.4
elif categoria==5:
    aumento=sueldo+sueldo*0.6
#Salida
print(aumento)

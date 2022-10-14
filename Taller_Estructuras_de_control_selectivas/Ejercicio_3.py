#Entrada
datos=input()
(a,b,c,d)=datos.split(" ")
a= int(a)
b= int(b)
c= int(c)
d= int(d)
resultado=0

#Caja negra

if d==0:
    resultado=(a-c)**2
elif d>0:
    resultado=((a-b)**3)/d
resultado=round(resultado,2)
#Salida
print(resultado)
import math
#Entradas
datos=input()
(a,b,c)=datos.split(" ")
a=float(a)
b=float(b)
c=float(c)
#Caja negra
z=(b**2)-4*a*c
if z<0 and a==0:
    print("Inpossible calcular")
else:
    x1=((-b+math.sqrt(z))/(2*a))
    x1=round(x1,5)
    x2=((-b-math.sqrt(z))/(2*a))
    x2=round(x2,5)
    print("R1=", x1, "R2=",x2)
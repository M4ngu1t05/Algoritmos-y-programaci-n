#Entrada
S= int(input(("Ingrese salario base: ")))
v1= int(input(("Ingrese el valor de la primera venta: ")))
v2= int(input(("Ingrese el valor de la segunda venta: ")))
v3= int(input(("Ingrese el valor de la tercera venta: ")))
#Caja negra
c1=v1*0.1
c1=round(c1,2)
c2=v2*0.1
c2=round(c2,2)
c3=v3*0.1
c3=round(c3,2)
cT=c1+c2+c3
#Salidas
print("El vendedor recibe unas comisiones de: "+str(cT)+" un total de: "+ str(cT+S))

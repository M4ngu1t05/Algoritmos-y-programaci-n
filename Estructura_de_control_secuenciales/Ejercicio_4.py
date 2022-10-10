#Entradas
from ast import Str


tC= int (input("Ingrese el costo de la compra: "))
#Caja negra
D= float (tC*0.15)
D= round (D,1)
T=tC-D
#Salidas
print ("El costo final del producto es de:", T ,"Con un descuento aplicado de:", D)
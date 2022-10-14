#Entrada
sueldo=float (input("Sueldo: "))
#Caja negra
sb=0
if sueldo<900000:
    sb=sueldo+(sueldo*0.15)
elif sueldo>=900000:
    sb=sueldo+(sueldo*0.12)
#Salidas
print ("nuevo sueldo es "+str(sb))
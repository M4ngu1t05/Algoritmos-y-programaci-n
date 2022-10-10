#Entradas
from re import S


hT= float (input("Cantidad de horas trabajadas: "))
pH= float (input("Precio de la hora laboral: "))
sB= float (input("Valor sueldo base: "))
#Caja negra
sN=(hT*pH+sB*0.2)
#Salidas
print("El sueldo neto del trabajador es de:", sN)
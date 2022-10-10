#Entradas
nombre= input("Ingrese el nombre del trabajador(a): ")
sueldo= float (input("Ingrese el sueldo del trabajador(a): "))
horasT= int (input ("Ingrese horas trabajadas por el trabajador(a): "))
horaN= float (input("Ingrese el costo de la hora normal: "))
horasE= int (input("Ingrese cantidad de horas extras trabajadas: "))
hijos= int (input("Ingrese la cantidad de hijos del trabajador(a): "))
#Caja negra
horastT=horasT*horaN
tHorasE=(horaN*0.25+horaN)*horasE
Deduccion=sueldo-(sueldo*0.05)-(sueldo*0.02)-(sueldo*0.07)
Deduccion=round(Deduccion,0)
Asignacion=250000+173000*hijos+180000
Total=sueldo+horastT+tHorasE-Deduccion+Asignacion
Total=round(Total,0)
#Salidas
print("El trabajador(a)", nombre, "recibe un total de:", Total, " con unas deducciones de:", Deduccion, "unas asignaciones de:", Asignacion, "y un total por horas extra de:",tHorasE)
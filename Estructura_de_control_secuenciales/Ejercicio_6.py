#Entradas
c= int (input("Ingrese cantidad de estudiantes: "))
ch= int (input ("Ingrese cantidad de estudiantes hombres: "))
cm= int (input("Ingrese cantidad de estudiantes mujeres: "))
#Caja negras
CH=(ch/c)*100
CH=round(CH,2)
CM=(cm/c)*100
CM=round(CM,2)
#Salida
print("El porcentaje de hombres es de:", CH,"% y el de mujeres es de:", CM,"%")
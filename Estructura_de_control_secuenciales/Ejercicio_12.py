#Entradas
ExamenM= float(input("Ingrese la nota del examen de matemáticas: "))
M1=float(input("Ingrese las notas de las tareas de matemáticas: "))
M2=float(input())
M3=float (input())
ExamenF=float(input("Ingrese la nota del examen de fisica: "))
F1=float(input("Ingrese las notas de las tareas de fisica: "))
F2=float(input())
ExamenQ=float(input("Ingrese la nota del examen de quimica: "))
Q1=float(input("Ingrese las notas de las tareas de quimica: "))
Q2=float(input())
Q3=float(input())
#Caja negra
PM=((ExamenM)*0.9+((M1+M2+M3)/3)*0.1)
PF=((ExamenF)*0.8+((F1+F2)/2)*0.2)
PQ=((ExamenQ)*0.85+((Q1+Q2+Q3)/3)*0.15)
PG=(PM+PF+PQ)/3
#Salidas
print("Promedio general: ",PG,", promedio de matemáticas:",PM,", promedio de fisica:",PF,"y promedio de quimica:",PQ)
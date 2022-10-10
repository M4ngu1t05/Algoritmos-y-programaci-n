#Entradas
K=float(("ingrese el costo por kilovatio del mes anterior anterior "))
k=float(("ingrese el costo por kilovatio del mes actual anterior "))
lecturaAnterior=float(input("ingrese la lectura del mes anterior anterior "))
lecturaActual=float(input("ingrese la lectura del mes anterior actual "))
#Caja negra
T=lecturaActual*k+lecturaAnterior*K
#Salidas
print("El total a pagar es de:", T)
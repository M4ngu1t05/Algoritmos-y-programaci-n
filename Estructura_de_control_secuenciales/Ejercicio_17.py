#Entradas
presupuesto=float(input("Ingrese el presupuesto para el hospital"))
#Caja negra
G=presupuesto*0.4
G=round(G,2)
T=presupuesto*0.3
T=round(T,2)
P=presupuesto*0.3
P=round(P,2)
#Salidas
print("El presupuesto de ginecologia es de:",G," el de traumatologia de:",T,"y el de pediatria:",P)
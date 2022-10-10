#Entradas
cH= float (input("Ingrese cantidad de chelines austriacos: "))
dG= float (input("Ingrese cantidad de dracmas griegos: "))
p= float (input("Ingrese cantidad de pesetas: "))
#Caja negra
CH=cH*956.871/100
DG=(dG*88.607/100)/20.110
P1=p/122.499
P2=p*100/9.289
#Salidas
print("la cantidad de chelines austriacos a pesetas es:", CH)
print("la cantidad de dracmas griegos a francos franceses es:", DG)
print("la cantidad de pesetas en dolares es de:",P1, "y en liras italianas es de:", P2)
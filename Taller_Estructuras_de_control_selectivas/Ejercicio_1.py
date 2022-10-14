#Entrada
capital=int (input("Ingrese capital: "))
tasa= float (input("Ingrese tasa: "))
tiempo= int (input("Ingrese tiempo: "))
#Caja negra
I=capital*tasa*tiempo
total=0
if I>100000:
    total=(I*tasa*tiempo)+capital
else:
    total=I+capital
print("el total en la cuenta es de:",total)

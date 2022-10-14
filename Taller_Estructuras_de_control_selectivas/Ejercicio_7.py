#Entrada
distancia= int (input)
#Caja negra
pago=0
if distancia<300:
    pago=50000
elif distancia>300:
    if distancia<1000:
        pago=70000+(distancia-300)*30000
    else:
        distancia>1000
        pago=150000+(distancia-300)*9000
print("el total a pagar es de", pago)
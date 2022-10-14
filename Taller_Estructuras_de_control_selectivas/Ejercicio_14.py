#Entrada
lecturaMesActual=int (input("Mes actual"))
lecturaMesAnterior= int (input("Mes anterior"))
#Caja negra
Monto=(abs(lecturaMesAnterior-lecturaMesActual))
pago=0
if Monto>=0 and  Monto<=100:
    pago=Monto*4600
elif Monto>100 and Monto<301:
    pago=Monto*80000
elif Monto>=301 and Monto<=500:
    pago=Monto*100000
elif Monto>=501:
    pago=Monto*120000
else:
    pago="Imposible calcular"
print ("El total a pagar es de:",pago)

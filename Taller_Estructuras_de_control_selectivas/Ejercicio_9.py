#Entrada
compra= float (input("compra: "))
#Caja negra
descuento=0

if compra<50000:
    descuento=0
    print ("No hay descuento")
elif compra >=50000 and compra<=100000:
    descuento=compra-compra*0.05
    print("el descuento es de:", descuento)
elif compra>=100000 and compra <= 700000:
    descuento =compra-compra*0.11
    print("el descuento es de:", descuento)
elif compra>=700000 and compra<=1500000:
    descuento=compra-compra*0.18
    print("el descuento es de:", descuento)
elif compra>1500000:
    descuento=compra-compra*0.25
    print("el descuento es de:", descuento)
descuento=round(descuento,2)
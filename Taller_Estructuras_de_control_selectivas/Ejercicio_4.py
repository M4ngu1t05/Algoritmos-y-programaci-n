#Entrada
compra= int (input())
#Caja negra
I=0
banco=0
r=0
c=0
if compra>5000000:
    I=compra*0.55
    I=round(I,2)
    banco= compra*0.3
    banco=round(banco,2)
    r= compra*0.15
    r=round(r,2)
    c=r*0.2
    c=round(c,2)
    print("la empresa pagará de sus fondos", I, ", por prestamo del banco",banco,", por crédito del fabricante",r, "y por intereses por crédito", c)
else:
    compra<= 5000000
    I= compra*0.7
    I=round(I,2)
    r=compra*0.3
    r= compra*0.15
    c=r*0.2
    c=round(c,2)
    print("la empresa pagará de sus fondos", I,", por crédito del fabricante",r, "y por intereses por crédito", c)


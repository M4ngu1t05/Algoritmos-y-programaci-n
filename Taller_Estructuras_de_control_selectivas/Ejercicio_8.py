#Entrada
P= int(input())
Q= int(input())
#Caja negra
s=""
r=P**3+Q**4-2*P**2
if r>680:
    s= (P,"y", Q,"satisfacen la expresión")
else:
    s= (P,"y", Q,"no satisfacen la expresión")
print(s)
A={}
B=[]
C=[]
D=[]
for i in range(1,11):
    nom=str(input("nombre: "))
    nota=float(input("nota: "))
    A.update({i:{'nombre': nom,'nota': nota}})
    D.append(nota)
    prom=sum(D)/(len(D))
    if(nota>=60):
        C.append(nom)
    print(f"aprobados son:{C}.")
    if(nota<60):
        B.append(nom)
    print(f"no aprobados son:{B}")
print(A)
print("El promedio es:",prom)
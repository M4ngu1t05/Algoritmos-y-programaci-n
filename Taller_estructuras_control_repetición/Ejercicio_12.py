N=int(input())
Nombres=[]
Puntajes=[]
J=0
L=0
Ñ=0
Q=0
def Mayor(Puntajes):
    max=Puntajes[0]
    for i in Puntajes:
        if i>max:
            max=i
    return max
def Menor(Puntajes):
    min=Puntajes[0]
    for i in Puntajes:
        if i<min:
            min=i
    return min

for _ in range (0,N):
    nombre=input("Nombre: ")
    puntaje=float(input("Puntaje: "))

    Nombres.append(nombre)
    Puntajes.append(puntaje)
    Union=list(zip(Nombres,Puntajes))


    for a,b in Union:
        Z=Mayor(Puntajes)
        Y=Menor(Puntajes)
        if b==Z:
            E=(f"{a} tiene el mayor puntaje")
        elif b==Y:
            K=(f"{a} tiene el menor puntaje")
        O=(f"{Z} es el mayor puntaje ")
        U=(f"{Y} es el menor puntaje ")

    for C in Puntajes:
        C=int(C)
        Ñ=Ñ+C
        J=Ñ/N
        P=(f"El promedio de puntajes es: {J}")
        if C<J:
            L=L+1
            Q=(L/N)*100
            M=(f"El porcentaje inferior al promedio es {Q}%")
        else:
            C>J
            L=L+1
            Q=(L/N)*100
            T=(f"El porcentaje mayor al promedio es {Q}%")
print(f"{E}\n{K}\n{O}\n{U}\n{P}\n{M}\n{T}")

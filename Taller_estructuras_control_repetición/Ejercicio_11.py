A=0
Mm=0
H=0
whisky=0
P=0
Z=0
cantidad=0

E=[]
while True:
    cantidad=cantidad+1
    
    Consume=bool(input("¿Consume licor? "))

    if Consume==True:

        licor=int(input("Licor preferido (1- Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))

        Edad=int(input("Edad: "))

        E.append(Edad)

        Sexo=input("Sexo: ")

        if  licor==5:
            whisky=whisky+1

        while True:
            if Consume==True:
             A=A+1
        
            if Sexo=="mujer" and Edad<18:
                Mm=Mm+1
            if Sexo=="hombre" and 20<=Edad<=25:
                if  licor!=1:
                    H=H+1
            if licor==5:
                Z=(whisky/cantidad)*100
            for i in E:
                if licor==3:
                    P=(P+i)/cantidad 
            print(f"Total personas encuestadas que consumen licor: {A}\nTotal de mujeres menores de edad: {Mm}\nTotal de hombres entre 20 y 25 que no toman aguardiente: {H}\npromedio de edades que toman cerveza: {P}\nporcentaje de personas que toman whiskey: {Z}")
            K=input("¿Desea continuar? ")
            if K==True:
                K=K
            else:
                K==False
                break
    else:
        print("No aplica para la encuenta")


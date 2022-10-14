#Entrada
H=float(input("Nivel de hemoglobina"))
Edad= int(input("Edad "))
Sexo= input("Sexo")
#Caja negra
mes=Edad*12
anemia=""
if mes >=0 and  mes <=1:
    if H>=0.13 and H<=0.16:
        anemia="Negativo"
    elif H>0.13:
        anemia="Positivo"
    else:
        anemia="Fuera de los parametros"
elif mes>1 and mes<=6:
    if H>=0.1 and H<=0.18:
        anemia="Negativo"
    elif H>0.1:
        anemia="Positivo"
    else:
        anemia="Fuera de los parametros"
elif mes>6 and mes<=12:
    if H>=0.11 and H<=0.15:
        anemia="Negativo"
    elif H>0.11:
        anemia="Positivo"
    else:
        anemia="Fuera de los parametros"
elif Edad>1 and Edad<=5:
    if H>=0.115 and H<=0.15:
        anemia="Negativo"
    elif H>0.115:
        anemia="Positivo"
    else:
        anemia="Fuera de los parametros"
elif Edad>5 and Edad<=10:
    if H>=0.126 and H<=0.155:
        anemia="Negativo"
    elif H>0.126:
        anemia="Positivo"
    else:
        anemia="Fuera de los parametros"
elif Edad>10 and Edad<=15:
    if H>=0.13 and H<=0.155:
        anemia="Negativo"
    elif H>0.13:
        anemia="Positivo"
    else:
        anemia="Fuera de los parametros"
elif Sexo=="Mujer":
    if Edad>15:
        if H>=0.12 and H<=0.16:
            anemia="Negativo"
        elif H>0.12:
            anemia="Positivo"
        else:
         anemia="Fuera de los parametros"
    else:
        anemia="Fuera de los parametros"
elif Sexo=="Hombre":
    if Edad>15:
        if H>=0.14 and H<=0.18:
            anemia="Negativo"
        elif H>0.14:
            anemia="Positivo"
        else:
         anemia="Fuera de los parametros"
    else:
        anemia="Fuera de los parametros"
#Salida
print(anemia)
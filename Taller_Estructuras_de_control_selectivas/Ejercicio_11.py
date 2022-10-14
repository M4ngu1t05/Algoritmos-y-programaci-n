#Entrada
T=float(input("Ingrese temperatura"))
#Caja negra
deporte=""
if T>85 and T<100:
    deporte="Natación"
elif T>70 and T<=85:
    deporte="Tenis"
elif T>32 and T<=70:
    deporte="Golf"
elif T>10 and T<=32:
    deporte="Esquí"
elif T>-5 and T<=10:
    deporte="Marcha"
else:
    deporte="Temperatura fuera de medición"
print (deporte)

usuarios = { 
 "iperurena": { 
 "nombre": "Iñaki", 
 "apellido": "Perurena", 
 "password": "123123" 
 }, 
 "fmuguruza": { 
 "nombre": "Fermín", 
 "apellido": "Muguruza", 
 "password": "654321" 
 }, 
 "aolaizola": { 
 "nombre": "Aimar", 
 "apellido": "Olaizola", 
 "password": "123456" 
 } 
 }
intentos=0

for key in usuarios: 
    t=usuarios[key]

A=("iperurena" in usuarios) 
B=("password" in t) 

while True:
    if(intentos==3):
        print("Demasiados intentos.")
        break
    C=str(input("Digite su usuario: "))
    D=int(input("Digite su contraseña: "))
    if((C=="iperurena" and A==True) and (D==123123 and B==True)):
        E= usuarios["iperurena"]
        E.pop("password")
        print(E)
        break
    elif((C=="fmuguruza" and A==True) and (D==654321 and B==True)):
        F= usuarios["fmuguruza"]
        F.pop("password")
        print(F)
        break
    elif((C=="aolaizola" and A==True) and (D==123456 and B==True)):
        G= usuarios["aolaizola"]
        G.pop("password")
        print(G)
        break
    else:
        intentos+=1
        print("Error al ingresar. Vuelva a intentarlo.")
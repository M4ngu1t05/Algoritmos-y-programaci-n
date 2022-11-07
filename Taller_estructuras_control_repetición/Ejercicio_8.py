X=True
while X:
    password=int(input())
    
    if password==2002:
        X=False
        print("Acesso Permitido")
    else:
        print("Senha inválida")
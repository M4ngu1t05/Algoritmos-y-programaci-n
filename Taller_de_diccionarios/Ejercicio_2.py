Ejemplo={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
Resultado=[]
for i in Ejemplo:
    N=(Ejemplo[i])
    Resultado.append(N)
    E=set(Resultado)
    A=list(E)
print(A)
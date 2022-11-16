Ejemplo=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
Resultado={12: 3, 23: 2, 5: 3, 92: 2, 29: 1, 64: 1}
for i in Ejemplo:
    C=Ejemplo.count(i)
    Resultado.update({i:C})
print(Resultado)
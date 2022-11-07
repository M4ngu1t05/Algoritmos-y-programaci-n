T=0
Z=0
H=0
for k in range (1,500):
    T=((k**2+1)/k)
    Z=Z+T
    if Z<=1000:
        H=H+1
print(H)

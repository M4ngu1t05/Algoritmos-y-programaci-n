A=[]
H=0

def Mayor(A):
    max=A[0]
    for i in A:
        if i>max:
            max=i
    return max

for _ in range (0,10):
    n=float(input())
    A.append(n)
    H=H+1
print(Mayor(A))

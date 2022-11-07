N=30
K=2
for _ in range (0,10000):
    if K<N:
        N=N-1
        if  K==N:
            break
        print(N)
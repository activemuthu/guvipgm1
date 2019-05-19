D,K=input().split()
D=int(D)
K=int(K)
for c in range (D+1,K):
    if c % 2 != 0:
        print(c,end=" ")

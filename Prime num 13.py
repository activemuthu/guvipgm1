N=int(input())
for c in range(2,N):
    if(N%c==0):
        print("no")
        break
else:
    print("yes")

D=input()
n=0
m=0
for c in D:
    if(c.isalpha()):
        n+=1
    elif(c.isnumeric()):
        m+=1    
if(m>0 and n>0):
    print("Yes")
else:
    print("No")

h, m =input().split()
h=int(h) 
m=int(m) 
for j in range(h+1,m):
  S=0
  for c in range(2,j):
    if j % c == 0:
      S= S+ 1
  if S==0:
      print(j,end="")

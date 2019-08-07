N=int(input())
if(N>=1 and N<=100000):
  l=list(map(int,input().split(" ")))
  if(l.count(0)==N):
    print("0")
  else:
    l.sort(reverse=True)
    s=""
    for j in l:
      s+=str(j)
    print(s)

n=int(input())
if(n>=1 and n<=100000):
  l=list(map(int,input().split(" ")))
  for j in l:
    if(l.count(j)==1):
      print(j)
      break

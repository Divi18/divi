n=int(input())
if(n>=1 and n<=100000):
  l=list(map(int,input().split(" ")))
  for i in l:
    if(l.count(i)==1):
      print(i)
      break

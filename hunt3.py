N=int(input())
if(N>=1 and N<=100000):
  l=list(map(int,input().split(" ")))
  flag=0
  for i in l:
    if(l.count(i)>1):
      l1=i
      flag=1
      break
  if(flag==1):
    print(l1)
  else:
    print("unique")

n=int(input())
if(n>=1 and n<=100000):
  l=list(map(int,input().split(" ")))
  l1=[]
  for i in range(0,len(l)):
    if(i==l[i]):
      l1.append(i)
  if(len(l1)==0):
    j=-1
    print(j)
  else:
    l1.sort()
    for i in range(0,len(l1)-1):
      print(l1[i],end=" ")
    print(l1[len(l1)-1])

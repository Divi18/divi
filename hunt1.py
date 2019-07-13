n=int(input())
l=[]
if(n>0 and n<10000):
  for i in range(0,n):
    l.append(int(input())
  l2=set(l)
  for i in l2:
    if l.count(i)>1:
      l1.append(i)
   if(l1==[]):
    print("unique")
   else:
    l1.sort()
    s=""
    for i in l1:
      s+=" "+str(i)
    print(s)
    


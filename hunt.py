N=int(input())
if(N>=1 and N<=100000):
  l=list(map(int,input().split(" ")))
  l1=[]
  for i in l:
    if l.count(i)>0:
      if i in l1:
        continue
      else:
        l1.append(i)
l1.sort()
s=""
for i in l1:
  s+=str(i)+" "
print(s)

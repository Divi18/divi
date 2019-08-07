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
  for i in range(0,len(l1)-1):
    s+=str(l1[i])+" "
  s+=str(l1[len(l1)-1])
  print(s[0:len(s)])

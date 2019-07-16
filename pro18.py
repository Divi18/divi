n1,m1=map(int,input().split())
l1=[]
for _ in range(n):
  l1.append(input())
for i in range(len(l1)):
  if('0' in l1[i]):
    l1[i]=l[i].replace('0','')
  l1[i]=l1[i].replace(' ','')
length=[]
for i in l1:
  if(len(i)>0):
    length.append(len(i))
m1=min(length)
r1='1 '*m1
r1=r1.strip()
for i in range(m1):
  print(r1)

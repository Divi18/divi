x1=input().split()
x1=[int(i) for i in x1]
k=x1[1]
flag=False
l1=input().split()
l1=[int(i) for i in l1]
for i in range(0,x1[0]):
  for j in range(i+1,x1[0]):
    t=l1[i]+l1[j]
    if(t==k):
      flag=True
      break
  if(flag):
    print("yes")
    break
if not(flag):
  print("no")

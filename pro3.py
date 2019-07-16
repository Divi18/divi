a1,b1=input().split()
l1=len(a1)
l2=len(b1)
mi=abs(l1-l2)
if(l1<=l2):
  s1=a1
  l3=b1
else:
  s1=b1
  l3=a1
if(len(s1)==1):
  print(mi)
else:
  for i in range(len(s1)):
    if(s1[i]!=l3[i]):
      mi+=1
  print(mi)

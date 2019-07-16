bc=int(input())
s1=list(map(int,input().split()))
a1=0
for i in range(bc):
  for j in range(i,bc):
    for k in range(j,bc):
      if(s1[i]<s1[j]<s1[k]):
        a1+=1
print(a1)

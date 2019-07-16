a1=int(input())
s1=0
for j in range(0,a1):
  if(pow(2,j)>a1):
    break
  s1=a1-pow(2,j)
print(s1)

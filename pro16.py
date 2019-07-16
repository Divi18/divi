n1=int(input())
l1=list(map(int,input().split()))
p1=[1]*n1
for i in range(n1):
  if(i==0 and l1[i]>l1[i+1]):
    p1[i]+=p1[i+1]
  if(i>0 and l1[i]>l1[i-1]):
    p1[i]+=p1[i-1]
print(sum(p1))

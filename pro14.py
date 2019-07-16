p1,q1=map(int,input().split())
l1=list(map(int,input().split()))
for i in range(q1):
  r1,s1=map(int,input().split())
  t1=l[r1-1:s1]
  u1=t1[0]
  for i in range(1,len(t1)):
    u1=u1^t1[i]
   print(u1)

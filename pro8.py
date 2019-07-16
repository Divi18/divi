import math
p1,q1=map(int,input().split())
rr=[]
ss=list(map(int,input().split()))
for i in range(0,q1):
        uu,vv =map(int,input().split())
        rr.append([uu,vv])
for i in rr:
        xx=i[0]-1
        yy=i[1]-1
        print(math.gcd(ss[xx],ss[yy]))

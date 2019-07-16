import math
p1,q1=map(int,input().split())
rr=[]
ss=list(map(int,input().split())
for i in range(0,q1):
        u1,v1=map(int,input().split())
        rr.append([u1,v1])
for i in rr:
        xx=i[0]-1
        yy=i[1]-1
        print(math.gcd(ss[xx],ss[yy]))

a,b=map(int,input().split())
arr=list(map(int,input().split(None,a)[:a]))
f1=[]
for i in range(b):
  d1,g1=map(int,input().split())
  f1.append(min(arr[d1-1:g1]))
for i in f1:
  print(i)

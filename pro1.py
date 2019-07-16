i=int(input())
arr=[]
for j in range(0,i):
  arr.append(input())
v=min(arr,key=len)
arr.remove(v)
for k in range(len(v)):
  for j in range(len(arr)):
    c=arr[j]
    if(v[:k+1]==c[:k+1]):
      r=v[:k+1]
    else:
      break
print(r)

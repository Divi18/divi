a1,b1=map(str,input().split())
y1=0
if(len(a1)>len(b1)):
  a1,b1=b1,a1
z1=0
while(z1<len(a1)):
  y1+=(ord(b1[z1])-ord(a1[z1]))
  z1+=1
for z1 in range(z1,len(b1)):
  y1+=ord(b1[z1)-ord('a')+1
print(y1)

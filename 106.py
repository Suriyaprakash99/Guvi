a,b=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
  if l[i]%2!=0:
    l1.append(l[i]) 
print(l[b-1])

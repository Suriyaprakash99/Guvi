a=[int(x) for x in input().split()]
lst=[]
for i in range(0,len(a)):
  if(i%2==0):
    if(a[i]%2!=0):
      lst.append(a[i])
  else:
    if(a[i]%2==0):
      lst.append(a[i])
for i in lst:
  print(i,end=" ")
      

  

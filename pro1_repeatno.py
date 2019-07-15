a=input("")
a1=list(a.split(" "))
#print(a1)
b=[]
for i in range(0,len(a1)):
  for j in range(i+1,len(a1)):
    if(a1[i]==a1[j]):
      #print(a1[i])
      if a1[i] not in b:
        b.append(a1[i])
#print(b)
c=" ".join(b)
print(c)

a,c=input("").split()
n=int(len(a))
c=int(c)
b=a[n-c]
for i in range(n-(c-1),n):
  b+=a[i]
print(b)


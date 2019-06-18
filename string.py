a=input("")
n=int(len(a))
print(n)
c=int(input())
b=a[n-c]
for i in range(n-(c-1),n):
  b+=a[i]
print(b)

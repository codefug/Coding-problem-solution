n=int(input())
a=1000000
b=1
k=list(map(int,input().split())
for i in range(n):
    if k[i]<=a:
        a=k[i]
    if k[i]>=b:
        b=k[i]
print(a,b)

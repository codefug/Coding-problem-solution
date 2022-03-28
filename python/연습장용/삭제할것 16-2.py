n=int(input())
n1=1
n0=0
for i in range(n-1):
    if i%2==1:
        pren0=n0+n1-1
    else:
        pren0=n0+n1
    pren1=n0+n1
    n0=pren0
    n1=pren1    
print(n0)

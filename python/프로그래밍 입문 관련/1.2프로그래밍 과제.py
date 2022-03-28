N=int(input("N="))
n=1
m=1
j=1
while n<=N:
    while j<=m and n<=N:
        print(n,end=' ')
        n+=1
        j+=1
    if n!=N:
        print()
    j=1
    m=m*2

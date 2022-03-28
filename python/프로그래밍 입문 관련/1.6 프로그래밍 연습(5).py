def isPerfect(m):
    t=0
    for i in range(1,m):
        if m%i==0:
            t+=i
    if t==m:
        return True

N = int(input('N = '))
for i in range(1, N+1):
    if isPerfect(i):
        print(i, end=' ')

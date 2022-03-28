#1929 소수 구하기

m,n=map(int,input().split())
if n<2:
    print(0)
    exit()
else:
    l=[1 for i in range(n+1)]
    l[0],l[1]=0,0
    for i in range(2,n//2+1):
        for j in range(i,n//2+1):
            if i*j>n:
                break
            l[i*j]=0
        
for i in range(m,len(l)):
    if l[i]:
        print(i)
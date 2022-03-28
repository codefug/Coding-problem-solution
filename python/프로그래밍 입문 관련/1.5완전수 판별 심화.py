def isthatPerfect(x):
    t=0
    for i in range(1,x):
        if x%i==0:
            t+=i
    if t==x:
        return True

N=int(input("N 입력:"))
while N<=2:
    print(N,"은 2보다 큰 자연수여야 합니다.")
    N=int(input("N 입력:"))
for j in range(2,N+1):
    if isthatPerfect(j):
        print(j,end=' ')

def panbeol(n):
    t=0
    for i in range(1,n):
        if n%i==0:
            t+=1
    if t==1:
        return True
    else:
        return False

N=int(input("2 이상의 자연수 입력:"))
while N<2:
    print(N,"은(는 2 이상의 자연수가 아닙니다.")
    N=int(input("2 이상의 자연수 입력:"))
for i in range(1,N+1):
    if panbeol(i):
        print(i,end=' ')


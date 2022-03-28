N=int(input("N="))
n=1
a=int(input("홀수/짝수 선택(1:홀수,2:짝수):"))
if a==1:
    while n<=N:
        if n%2==1:
            print(n,end=' ')
        n+=1
if a==2:
    for i in range(1,N+1):
        if i%2==0:
            print(i,end=' ')

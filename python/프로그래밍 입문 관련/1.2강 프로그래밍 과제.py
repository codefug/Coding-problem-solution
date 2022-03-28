n=int(input("자연수 입력:"))
while n<=0:
    print(n,"은 자연수가 아닙니다.")
    n=int(input("자연수 입력:"))
print(n,"의 모든 약수:",end='')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')

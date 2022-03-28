n=int(input("2이상의 자연수 입력:"))
t=0
for i in range(1,n):
    if n%i==0:
        t+=1
if t==1:
    print(n,"은(는) 소수입니다.")
else:
    print(n,"은(는) 소수가 아닙니다.")


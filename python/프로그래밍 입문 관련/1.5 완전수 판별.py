n=int(input("자연수 입력:"))
t=0
for i in range(1,n):
    if n%i==0:
        t+=i
if t==n:
    print(n,"은(는) 완전수입니다.")
else:
    print(n,"은(는) 완전수가 아닙니다.")
    

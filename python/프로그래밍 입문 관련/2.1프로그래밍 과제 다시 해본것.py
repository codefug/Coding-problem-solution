import time
N=int(input("2 이상의 자연수 입력:"))
start=time.time()
b=0
a=list((range(N+1)))
a[1]=0
i=2
while i<=N/2:
    j=i
    while i*j<=N and a[i]!=0:
        a[i*j]=0
        j+=1
    i+=1
            
for i in range(N+1):
    if a[i]!=0:
        b+=1
print("실행시간",time.time()-start)
print(b,"개의 소수 발견")

    

'''
ver.1
'''
import time
start=time.time()
N=int(input("N="))
a=list(range(N+1))
for i in range(2,N//2+1):
   for j in range(i,N//2+1):
       if i*j<=N:
           a[i*j]=0
print("에라토스테네스의 체를 이용한 소수 리스트:")
for i in range(2,N+1):
    if a[i]:
        print(a[i],end='  ')
end=time.time()-start
print('')
print("실행시간",end)
'''
교수님 피셜

N = int(input('N = '))
a = list(range(N+1))
a[1] = 0
for i in range(2, int(N/2)+1):
    for j in range(i, int(N/2)+1):
        if i*j <= N and a[i*j] == 0:
            continue
        if i*j <= N:
            a[i*j] = 0
        else:
            break
for i in range(N+1):
    if a[i]:
        print(a[i], end=' ') 
'''
'''
ver.2
'''
N=int(input("N="))
a=[0]*(N+1)
for i in range(2,N//2+1):
    if a[i]==0:
        for j in range(2*i,N+1,i):
            a[j]=1
for i in range(2,N+1):
    if a[i]==0:
        a[i]=i
    if a[i]==i:
        print(a[i],end='  ')

            

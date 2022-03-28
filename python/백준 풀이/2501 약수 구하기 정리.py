#2501 약수 구하기

n,k=map(int,input().split())

j=0

for i in range(1,n+1):

    if n%i==0:

        j+=1

        if j==k:
            
            break

print(i if j==k else 0)

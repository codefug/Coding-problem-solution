import random
n=int(input("리스트의 원소개수:"))
k=int(input("목표값:"))
t=[]
for i in range(n):
    r=random.randint(1,2*n)
    t.append(r)
print(t)
for i in range(n-1):
    for j in range(i+1,n):
        if t[i]+t[j]==k:
            print("%d번째와 %d번째 원소"%(i+1,j+1))
    

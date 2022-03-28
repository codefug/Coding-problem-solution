import random
n=int(input("리스트의 원소 개수:"))
k=int(input("목표값:"))
t=[]
for i in range(n):
    t.append(random.randint(1,2*n))
print(t)
for i in range(len(t)-1):
    for j in range(i,len(t)):
        if t[i]+t[j]==k:
            print("%d번째 원소와 %d번째 원소"%(i,j))


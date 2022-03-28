import random
t=[]
n=int(input("리스트의 원소 개수 입력:"))
for i in range(n):
    r=random.randint(1,2*n)
    t.append(r)
print("리스트:",t)
k=int(input("목표값 입력:"))
print("두 수의 합이",k,"인 원소 쌍")
for i in range(n-1):
    for j in range(i+1,n):
        if t[i]+t[j]==k:
            print('%d번째와 %d번째 원소'%(i+1,j+1))

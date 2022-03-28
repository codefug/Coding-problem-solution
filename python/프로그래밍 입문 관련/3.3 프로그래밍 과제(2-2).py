#중복이 없는 정렬된 리스트 난수
import random
n=int(input("난수 입력:"))
T=[]
t=[]
for i in range(n):
    r=random.randint(1,n)
    t.append(r)
print(t)
for j in range(len(t)):
    if T.count(t[j])==0:
        T.append(t[j])
print(T)
T.sort()
print(T)
print("리스트 출력:",T)

import random
n=int(input("데이터의 개수 입력:"))
t=[]
for i in range(n):
    r=random.randint(1,50)
    t.append(r)
t.sort()
print("리스트:",t)
k=int(input("탐색 키 입력:"))
if t[n//2]>k:
    for j in range(0,n//2):
        if t[j]==k:
            print(f"{j+1}번째 위치에서 탐색키와 동일한 원소 발견")
            i=1
            break
else:
    for j in range(n//2,n+1):
        if t[j]==k:
            print(f"{j+1}번째 위치에서 탐색키와 동일한 원소 발견")
            i=1
            break
if i!=1:
    print("탐색 키와 동일한 원소가 없습니다.")

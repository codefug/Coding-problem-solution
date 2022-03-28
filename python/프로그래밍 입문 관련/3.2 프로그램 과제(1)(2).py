import random
n=int(input("리스트의 원소 개수입력:"))
t=[]
T=[]
for i in range(n):
    r=random.randint(1,2*n)
    t.append(r)
t.sort()
for i in range(len(t)):
    if T.count(t[i])==0:
        T.append(t[i])
print("정렬된 리스트:",t)
print("중복이 제거된 리스트:",T)
k=int(input("k="))
print("두 수의 합이",k,"인 원소 쌍")
i=0
j=len(T)-1
while i<j:
    if T[i]+T[j]==k:
        print('%d 번째와 %d 번째 원소'%(i+1,j+1))
        i+=1
        j-=1
    elif T[i]+T[j]>k:
        j-=1
    else:
        i+=1
    print(i)
    print(j)
    

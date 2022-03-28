import random
n=int(input("리스트의 원소 개수 입력:"))
line=[]
l1=[]
l2=[]
for i in range(n):
    r=random.randint(1,100)
    line.append(r)
line.sort()
for i in range(n//2):
    l1.append(line[i])
for j in range(n//2,n):
    l2.append(line[j])
l1.sort()
l2.sort()
l3=l1+l2
l3.sort()
print("최초 리스트:",line)
print("정렬된 첫번째 리스트:",l1)
print("정렬된 두번째 리스트:",l2)
print("합병된 리스트:",l3)

import random
r1=int(input("첫 번째 리스트의 원소 개수 입력:"))
r2=int(input("두 번째 리스트의 원소 개수 입력:"))
l1=[]
l2=[]
for i in range(r1):
    l1.append(random.randint(1,100))
for j in range(r2):
    l2.append(random.randint(1,100))
l1.sort()
l2.sort()
print("정렬된 첫 번째 리스트:",l1)
print("정렬된 두 번째 리스트:",l2)
l3=l1+l2
l3.sort()
print("합병된 리스트:",l3)

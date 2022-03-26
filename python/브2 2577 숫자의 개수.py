#2577 숫자의 개수

a=int(input())
b=int(input())
c=int(input())

list=[0 for i in range(10)]

numb=str(a*b*c)

for i in range(len(numb)):
    
    list[int(numb[i])]+=1
    
for i in range(10):
    
    print(list[i])
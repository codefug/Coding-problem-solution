#4153 직각삼각형

from itertools import permutations

a,b,c=map(int,input().split())
answer=[]
while a!=0 and b!=0 and c!=0:

    flag=0
    
    for q,w,e in permutations((a,b,c),3):
        
        if q**2+w**2==e**2:
            answer.append("right")
            flag=1
            break
    
    if flag==0:
        answer.append("wrong")
        
    a,b,c=map(int,input().split())
    
for i in answer:
    print(i)
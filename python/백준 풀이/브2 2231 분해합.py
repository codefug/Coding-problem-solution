#2231 분해합

n=int(input())

for i in range(1,n+1):
    
    i=str(i)
    
    answer=int(i)
    
    for _ in range(len(i)):
        
        answer+=int(i[_])
        
    if answer==n:
        print(i)
        break

else:
    print(0)
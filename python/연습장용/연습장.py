#1874

import sys

input=sys.stdin.readline

n=int(input())

message=True

j=0

answer=[]

stack=[]

for i in range(1,n+1):
    
    k=int(input()) 

    while j < k:
       
       j+=1
       
       answer.append("+")
       
       stack.append(j)
       
    if stack[-1]!=k:
        
        message=False
        
        continue
    
    else:
        
        answer.append("-")
        
        stack.pop()
        
if message==False:
    
    print("No")
    
else:
    
    print("\n".join(answer))
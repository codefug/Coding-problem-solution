#1874

from sys import stdin

input=stdin.readline

n=int(input())

count=0

stack=[]

answer=[]

message=True

for i in range(n):
    
    num=int(input())

    while count < num:
        
        count+=1
        
        stack.append(count)
        
        answer.append("+")
        
    if stack[-1]==num:
        
        answer.append("-")
        
        stack.pop()
        
    else:
        
        message=False
        
        break
    
if message==True:
    
    print("\n".join(answer))
    
else:
    
    print("NO")
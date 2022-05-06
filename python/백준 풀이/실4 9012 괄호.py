#9012 괄호

for i in range(int(input())):
    
    q=list(input())
    
    if q[0]==')':
        
        answer=0
        
    else:
        
        stack=['(']
        
        for i in range(1,len(q)):
                
            if stack and stack[-1]=='('!=q[i]:
                    
                stack.pop()
                    
            else:
                    
                stack.append(q[i])
                    
        if stack:
            
            answer=0
            
        else:
            
            answer=1    
            
    if answer==0:
        
        print('NO')
        
    else:
        
        print('YES')
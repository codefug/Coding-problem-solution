#2908 상수

def reversed(n):
    answer=0
    for i in range(3):
        
        answer*=10
        answer+=int(n[2-i])
                
    return answer

def solution(n1,n2):
    
    for i in range(3):
        
        if int(n1[2-i])>int(n2[2-i]):
            
            return reversed(n1)
        
        elif int(n1[2-i])<int(n2[2-i]):
            
            return reversed(n2)
            

num1,num2=input().split()

print(solution(num1,num2))
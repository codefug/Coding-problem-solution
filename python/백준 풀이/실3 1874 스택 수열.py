#1874 스택 수열

'''
 답지 보고 옴
 유의해야 할 점
 1.스택과 큐는 다르다. 원래 있는 스택에서 뒤에 있는 걸 빼고
 다른걸 채운다는 느낌으로 가야한다.
'''
stack=[0]

l=[]

n=int(input())

for i in range(n):
    
    l.append(int(input()))

j=0

answer=[]

for i in range(1,n+1):

    stack.append(i)
    answer.append("+")
    
    while j!=n and stack[-1]==l[j]:
        
        stack.pop()
        
        answer.append("-")
        
        j+=1
        
if j!=n:
    
    print("NO")
    
else:
    
    for i in answer:
        
        print(i)
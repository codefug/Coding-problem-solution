def pop(stack):
    if empty(stack):
        print("스택이 공백입니다.")
        return []
    else:
        return stack.pop()
def push(stack,x):
    stack.append(x)
    
def empty(stack):
    if len(stack)>0:
        return False
    else:
        return True

n=input("수식 입력:")
stack=[]
answer=[]
for i in range(len(n)):
    if ord(n[i])>47 and ord(n[i])<58:
        if i>0 and ord(n[i-1])>47 and ord(n[i-1])<58:
            a=pop(answer)
            push(answer,(int(a)*10)+int(n[i]))
        else:
            push(answer,n[i])
    elif n[i]=='(':
        push(stack,n[i])
    elif n[i]==')':
        push(stack,n[i])
        while pop(stack)!='(':
            push(answer,stack[-1])
        pop(answer)
    elif n[i]=='*' or n[i]=='/':
        if empty(stack) or stack[-1]=='+' or stack[-1]=='-':
            push(stack,n[i])
        elif stack[-1]=='*' or stack[-1]=='/':
            push(answer,pop(stack))
            push(stack,n[i])
    elif n[i]=='+' or n[i]=='-':
        if empty(stack):
            push(stack,n[i])
        elif stack[-1]=='*' or stack[-1]=='/' or stack[-1]=='+' or stack[-1]=='-':
            while empty(stack)!=True:
                push(answer,pop(stack))
            push(stack,n[i])
        else:
            push(stack,n[i])
while empty(stack)!=True:
    push(answer,pop(stack))
print("후위 표기식",answer)
        
            

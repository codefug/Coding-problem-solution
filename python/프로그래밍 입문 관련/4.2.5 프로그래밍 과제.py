#후위 표기식을 계산하여 계산 결과를 출력하는 프로그램 작성
def areplus(r1,r2):
    r3=float(r2)+float(r1)
    return r3
def areminor(r1,r2):
    r3=float(r2)-float(r1)
    return r3
def aremulti(r1,r2):
    r3=float(r2)*float(r1)
    return r3
def aredivid(r1,r2):
    r3=float(r2)/float(r1)
    return r3
def push(stack,x):
    stack.append(x)

def pop(stack):
    if empty(stack):
        print("스택이 공백입니다")
        return []
    else:
        return stack.pop()
def empty(stack):
    if len(stack)>0:
        return False
    else:
        return True


n=input("수식 입력:")
answer=[]
stack=[]
for i in range(len(n)):
    if n[i].isnumeric():
        if i!=0 and n[i-1].isnumeric():
            a=pop(answer)
            push(answer,str(int(a)*10+int(n[i])))
        else:
            push(answer,n[i])
    elif n[i]=='(':
        push(stack,n[i])
    elif n[i]==')':
        while stack[-1]!='(':
            push(answer,pop(stack))
        pop(stack)
    elif n[i]=='*' or n[i]=='/':
        if empty(stack):
            push(stack,n[i])
        elif stack[-1]=='*' or stack[-1]=='/':
            push(answer,pop(stack))
            push(stack,n[i])
        else:
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
n=answer
print("후위 표기식:",n)
stack=[]
answer=[]
for i in range(len(n)):
    if n[i].isnumeric():
        push(stack,str(n[i]))
        print(stack)
    elif n[i]=='*':
        push(stack,aremulti(pop(stack),pop(stack)))
        print(stack)
    elif n[i]=='/':
        push(stack,aredivid(pop(stack),pop(stack)))
        print(stack)
    elif n[i]=='+':
        push(stack,areplus(pop(stack),pop(stack)))
        print(stack)
    else:
        push(stack,areminor(pop(stack),pop(stack)))
        print(stack)
push(answer,stack[-1])
print('계산 결과 : %2f'%answer[0])

        
        
            

def pop(stack):
    if empty(stack):
        print("스택이 공백입니다")
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

def formyanswer(n):
    stack=[]
    postn=[]
    for i in range(len(n)):
        a=n[i]
        if ord(a)<58 and ord(a)>47:
            if i>=1 and ord(n[i-1])>47 and ord(n[i-1])<58:
                postn[-1]=f"{int(n[i-1])*10+int(n[i])}"
            else:
                push(postn,a)
                print("postn:",postn)
        elif a=='(':
            push(stack,a)
            print('stack:',stack)
        elif a==')':
            print('stack:',stack)
            while stack[-1]!='(':
                push(postn,pop(stack))
            pop(stack)
            print('stack:',stack)
            print('postn:',postn)
        elif a=='*' or a=='/':
            if empty(stack):
                push(stack,a)
            elif stack[-1]=='*' or stack[-1]=='/':
                push(postn,pop(stack))
                push(stack,a)
            else:
                push(stack,a)
        elif a=='+' or a=='-':
            if empty(stack):
                push(stack,a)
            elif stack[-1]=='*' or stack[-1]=='/' or stack[-1]=='+' or stack[-1]=='-':
                while empty(stack)!=True:
                    push(postn,pop(stack))
                push(stack,a)
            else:
                push(stack,a)
    while len(stack)!=0:
        push(postn,pop(stack))
    return postn
            
middlen=input("수식 입력:")
postn=formyanswer(middlen)
print("후위 표기식:",postn)

def push(stack,x):
    stack.append(x)
def empty(stack):
    if len(stack)==0:
        return True
    else:
        return False
def pop(stack):
    if empty(stack):
        return []
    else:
        return stack.pop()
def iswrong(l):
    if len(l)<=1:
        return True
    if l.count('(')!=l.count(')') or l.count('[')!=l.count(']'):
        return True
    if l[0]==')' or l[0]==']':
        return True
    t=[l[0]]
    for i in range(1,len(l)):
        if l[i]=='(':
            push(t,l[i])
        if l[i]=='[':
            push(t,l[i])
        if l[i]==')':
            if t[-1]=='(':
                pop(t)
            else:
                return True
        elif l[i]==']':
            if t[-1]=='[':
                pop(t)
            else:
                return True
    return False
l=list(input())
if iswrong(l):
    print(0)
else:
    result=0
    stack=[l[0]]
    for i in range(1,len(l)):
        if l[i]=='(':
            if l[i-1]==')' or l[i-1]==']':
                push(stack,'+')
            push(stack,l[i])
        elif l[i]=='[':
            if l[i-1]==')' or l[i-1]==']':
                push(stack,'+')
            push(stack,l[i])
        elif l[i]==')':
            if stack[-1]=='(':
                pop(stack)
                push(stack,2)
            else:
                result=pop(stack)
                while stack[-1]!='(':
                    n=pop(stack)
                    if n=='+':
                        n=pop(stack)
                        result+=n            
                pop(stack)
                result*=2
                push(stack,result)
        elif l[i]==']':
            if stack[-1]=='[':
                pop(stack)
                push(stack,3)
            else:
                result=pop(stack)
                while stack[-1]!='[':
                    n=pop(stack)
                    if n=='+':
                        n=pop(stack)
                        result+=n            
                pop(stack)
                result*=3
                push(stack,result)
    t=''
    for i in range(len(stack)):
            t+=str(stack[i])
    result=eval(t)
    print(result)

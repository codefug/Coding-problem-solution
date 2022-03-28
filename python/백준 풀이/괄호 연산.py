def push(l,x):
    l.append(x)
def pop(l):
    if len(l)==0:
        return []
    else:
        return l.pop()
stack=[]
l=list(input())
push(stack,l[0])
for i in range(1,len(l)):
    if l[i]=='(':
        if l[i-1]==')' or l[i-1]==']':
            push(stack,'+')
        push(stack,l[i])
    if l[i]=='[':
        if l[i-1]==')' or l[i-1]==']':
            push(stack,'+')
        push(stack,l[i])
    if l[i]==')':
        if stack[-1]=='(':
            pop(stack)
            push(stack,2)
        else:
            bfn=0
            while stack[-1]!='(':
                n=pop(stack)
                if bfn==0:
                    bfn=n
                elif n=='*':
                    m=pop(stack)
                    bfn=bfn*m
                elif n=='+':
                    m=pop(stack)
                    bfn=bfn+m
            pop(stack)
            bfn*=2
            push(stack,bfn)
    if l[i]==']':
        if stack[-1]=='[':
            pop(stack)
            push(stack,3)
        else:
            bfn=0
            while stack[-1]!='[':
                n=pop(stack)
                if bfn==0:
                    bfn=n
                elif n=='*':
                    m=pop(stack)
                    bfn=bfn*m
                elif n=='+':
                    m=pop(stack)
                    bfn=bfn+m
            pop(stack)
            bfn*=3
            push(stack,bfn)
result=pop(stack)
while len(stack)>1:
    if pop(stack)=='+':
        m=pop(stack)
        result=result+m
    elif pop(stack)=='*':
        m=pop(stack)
        result=result*m
print(result)

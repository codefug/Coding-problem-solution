def pop(stack):
    if empty(stack):
        print("스택이 공백이다")
        return []
    else:
        return stack.pop()
def empty(stack):
    if len(stack)>0:
        return False
    else:
        return True

def push(stack,x):
    stack.append(x)


def formyanswer(n,stack):
    l=len(n)
    if empty(stack):
        for i in range(l):
            if n[i]=='(':
                push(stack,n[i])
                print(stack)
            elif n[i]==')':
                if empty(stack):
                    return False
                pop(stack)
                print(stack)
    if empty(stack):
        return True
    else:
        return False
            


stack=[]
n=input("괄호가 있는 수식 입력:")
if formyanswer(n,stack):
    print('괄호쌍이 맞습니다')
else:
    print('괄호쌍이 맞지 않습니다.')
    

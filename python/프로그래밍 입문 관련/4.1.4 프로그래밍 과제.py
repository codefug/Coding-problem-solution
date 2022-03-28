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

def push(stack,x):
    stack.append(x)

def formyanswer(stack,n):
    for i in range(len(n)):
        if n[i]=='(' or n[i]=='[' or n[i]=='{':
            push(stack,n[i])
            print(stack)
        elif n[i]==')':
            if empty(stack):
                return False
            if pop(stack)!='(':
                return False
            else:
                print(stack)
        elif n[i]==']':
            if empty(stack):
                return False
            if pop(stack)!='[':
                return False
            else:
                print(stack)
        elif n[i]=='}':
            if empty(stack):
                print(stack)
                return False
            if pop(stack)!='{':
                print(stack)
                return False
            else:
                print(stack)
    if empty(stack):
        return True
    else:
        return False

stack=[]
n=input("괄호가 있는 수식 입력:")
if formyanswer(stack,n):
    print("괄호 쌍이 맞습니다.")
else:
    print("괄호 쌍이 맞지 않습니다.")

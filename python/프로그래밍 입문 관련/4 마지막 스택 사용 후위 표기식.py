def empty(stack):
    if len(stack)>0:
        return False
    else:
        return True

def pop(stack):
    if empty(stack):
        print("스택이 공백입니다")
        return []
    else:
        return stack.pop()
def push(stack,x):
    stack.append(x)



n=input("수식 입력:")
i=0
stack=[]
t=[]

    
    

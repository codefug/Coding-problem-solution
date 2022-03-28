def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        print('스택이 공백입니다.')
        return []
    else:
        return stack.pop()

def isEmpty(stack):
    if len(stack)>0:
        return False
    else:
        return True

stack=[]
tmp=pop(stack)
push(stack,'a')
print(stack)
push(stack,'b')
print(stack)
push(stack,'c')
print(stack)
tmp=pop(stack)
print(stack)
tmp=pop(stack)
print(stack)

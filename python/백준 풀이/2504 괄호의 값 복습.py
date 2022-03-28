#2504 괄호의 값 복습

def solution(l):

    stack=[]

    for i in range(len(l)):

        if l[i]=='(' or l[i]=='[':

            stack.append(l[i])

        elif l[i]==')':

            a=0

            while stack:

                item=stack.pop()

                if item=='(':

                    stack.append(2 if a==0 else a*2)

                    break

                elif item=='[':

                    return 0

                else:

                    a+=item

        elif l[i]==']':

            a=0

            while stack:

                item=stack.pop()

                if item=='[':

                    stack.append(3 if a==0 else a*3)

                    break

                elif item=='(':

                    return 0

                else:

                    a+=item


    return stack

l=list(input())

stack=solution(l)

if stack==0:

    stack=[]

print(0 if '(' in stack or '[' in stack else sum(stack))

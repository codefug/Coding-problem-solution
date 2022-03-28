def f(a,b):
    for i in range(len(a)):
        if a.count(b[i])!=b.count(b[i]):
            return False
    return True
        



a=input("a=")
b=input("b=")
A=[]
B=[]
for i in range(len(a)):
    if a[i].isalpha():
        A.append(a[i])
for i in range(len(b)):
    if b[i].isalpha():
        B.append(b[i])
if len(A)!=len(B):
    print("어구전철이 아닙니다")
elif f(A,B):
    print("어구전철입니다")
else:
    print("어구전철이 아닙니다")

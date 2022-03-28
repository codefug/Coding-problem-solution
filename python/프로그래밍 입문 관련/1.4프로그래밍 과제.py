a=int(input("자연수 a 입력:"))
b=int(input("자연수 b 입력:"))
c=int(input("자연수 c 입력:"))
A=a
B=b
C=c
while A!=B:
    if A<B:
        A+=a
    elif A>B:
        B+=b
T=A
while A!=C:
    if A<C:
        A+=T
    elif A>C:
        C+=c
print("최소공배수:",C)


a,b=input().split()
a=int(a)
b=int(b)
A=a
B=b
while A!=B:
    if A>B:
        B+=b
    else:
        A+=a
while a%b!=0:
    r=a%b
    a=b
    b=r
print(b,B)

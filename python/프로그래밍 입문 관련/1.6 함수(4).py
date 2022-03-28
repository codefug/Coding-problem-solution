def jegop(a,b):
    A=1
    for i in range(1,b+1):
        A*=a
    return A
a=int(input("a="))
b=int(input("b="))
print(jegop(a,b))

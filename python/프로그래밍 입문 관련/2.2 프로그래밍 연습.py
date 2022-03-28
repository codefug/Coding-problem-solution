def makeNum(x):
    n=len(x)
    s=0
    for i in range(n):
        s+=(ord(x[i])-48)*10**(n-1-i)
    return s

a=input('a=')
b=input('b=')
a=makeNum(a)
b=makeNum(b)
print(a+b)

def hanoi(n,a,b,c):
    if n==1:
        print("%s를 %s로"%(a,c))
    else:
        hanoi(n-1,a,c,b)
        print("%s를 %s로"%(a,c))
        hanoi(n-1,b,a,c)

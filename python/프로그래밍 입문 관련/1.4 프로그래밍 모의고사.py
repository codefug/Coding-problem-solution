def isPerfect(x):
    n=1
    N=0
    while n<x:
        if x%n==0:
            N+=n
        n+=1
    if x==N:
        answer=1
    if x<N:
        answer=2
    if x>N:
        answer=3
        
    return answer


a=int(input("a="))
b=int(input("b="))
while a<=b:
    if isPerfect(a)==1:
        print(a,": 완전수")
    if isPerfect(a)==2:
        print(a,":과잉수")
    if isPerfect(a)==3:
        print(a,":부족수")
    a+=1


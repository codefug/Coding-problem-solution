"""2 3 3 2 순으로 리스트를 만드는 프로그램 작성
12 345 678 910
"""
d=[]
a=1
c=2
while a<=10:
    t=[]
    b=1
    while b<=c and a<=10:
        t.append(a)
        a+=1
        b+=1
    if a==3:
        c+=1
    elif a==9:
        c-=1
    d.append(t)
print(d)

    
        
        

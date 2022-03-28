a=int(input("정수 입력(종료시는 999):"))
t=[]
while a!=999:
    if t.count(a)==0:
        t.append(a)
    a=int(input("정수 입력(종료시는 999):"))
t.sort()
print(t)

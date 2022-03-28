a=int(input("a="))#계수
x=int(input("x="))#항
e=int(input("e="))#지수
"""
e는 음이 아닌 정수 검사하고 다시 입력
x와 e가 0,0이면 1로 취급
출력값 g를 구해보자
"""
while e<0:
    print("e는 음이 아닌 정수입니다.")
    e=int(input("e="))
if x==0 and e==0:
    g=a
    print(g)
elif e==0:
    g=a
    print(g)
else:
    n=1
    g=x
    while n<e:
        g=g*x
        n+=1
    g=a*g
    print(g)

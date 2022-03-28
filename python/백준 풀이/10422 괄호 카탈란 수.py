#10422 카탈란 수 이용해 괄호 풀이
import math
f=math.factorial
t=int(input())
t_list=[]
for i in range(t):
    t_list.append(int(input()))
for i in range(t):
    n=t_list[i]
    if n%2==1:
        print(0)
    else:
        n//=2
        answer=f(2*n)//(f(n)*f(n+1))
        print(answer%1000000007)

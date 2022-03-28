#acmicpc/problem/1789 수들의 합
s=int(input()) #자연수s
i=0
n=0
a=1
while i<=s:
    if i==s:
        break
    else:
        i+=a
        a+=1
        n+=1
if i>s:
    n-=1
print(n)        

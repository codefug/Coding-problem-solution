def f(n):
    l=len(n)-1
    for i in range(l):
        if l>i:
            if n[i]!=n[l]:
                return False
        l-=1
    return True




n=input("문자열 입력:")
t=''
for i in range(len(n)):
    if n[i].isalnum():
        t+=n[i]
print("변환된 문자열:",t)
if f(t):
    print("회문입니다")
else:
    print("회문이 아닙니다")
    

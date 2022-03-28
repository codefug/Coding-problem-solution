def isalpha(n):
    N=''
    for i in range(len(n)):
        if n[i].isalpha():
            N+=n[i]
    return N

n=input("문자열 입력:")
print("변환된 문자열:",isalpha(n))
b=isalpha(n)
for i in range(len(b)//2+1):
    if b[i]!=b[len(b)-1-i]:
        print("회문이 아닙니다.")
        break

if i>=len(b)//2:
    print("회문입니다.")
    

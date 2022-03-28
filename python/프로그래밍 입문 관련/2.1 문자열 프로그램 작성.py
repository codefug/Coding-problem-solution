n=input("문자열 입력:")
s=len(n)
j=s-1
for i in range(s):
    if j>i:
        if n[j]!=n[i]:
            print("회문이 아닙니다")
            break
    j-=1
if j<i:
    print("회문입니다")
            

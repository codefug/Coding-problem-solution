N=input("문자열 입력:")
a=0
b=len(N)-1
while a<=b:
    if N[a]!=N[b]:
        print("회문이 아닙니다")
        break
    a+=1
    b-=1
if a>=b:
    print("회문입니다.")
    

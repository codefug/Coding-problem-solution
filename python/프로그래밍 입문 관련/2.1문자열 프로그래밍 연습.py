#첫 문자열 프로그래밍 연습
s=list(str(input("s=")))
n=len(s)
b=[]
for i in range(n):
    if b.count(s[i])==0:
        b.append(s[i])
print("중복이 제거된 문자열:",b)

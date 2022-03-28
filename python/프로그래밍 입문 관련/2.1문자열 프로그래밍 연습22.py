s=str(input("s="))
n=len(s)
t=''
for i in range(n):
    if t.count(s[i])==0:
        t+=s[i]
print("중복이 제거된 문자열:",t)

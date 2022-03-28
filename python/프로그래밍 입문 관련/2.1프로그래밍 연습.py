s=input("s=")
t=''
for i in range(len(s)):
    if t.count(s[i])==0:
        t+=s[i]
print("중복이 제거된 문자열:",t)

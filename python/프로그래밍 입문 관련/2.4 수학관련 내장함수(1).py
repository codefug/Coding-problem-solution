n=input("문자열 입력:")
m=len(n)
T=[]
i=0
while i<len(n):
    t=[]
    while i<len(n) and t.count(n[i])==0:
        t.append(n[i])
        i+=1
    
    T.append(t)
print("최장 부분문자열의 길이:",len(max(T)))

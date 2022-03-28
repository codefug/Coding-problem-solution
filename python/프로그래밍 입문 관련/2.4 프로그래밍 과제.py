n=input("문자열 입력:")
i=0
T=[]
while i<len(n):
    t=[]
    while i<len(n) and t.count(n[i])==0:
        t.append(n[i])
        i+=1
    T.append(t)
print("최장 부분문자열:",end='')
for i in range(len(max(T))):
    print(max(T)[i],end='')
    

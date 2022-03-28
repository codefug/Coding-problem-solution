from sys import stdin,exit
input=stdin.readline
def gotoantatica(idx,cnt):
    global max_result
    if cnt==0:
        result=0
        for i in l:
            for j in i:
                if not alpha[ord(j)-ord('a')]:
                    break
            else:
                result+=1
        max_result=max(max_result,result) if max_result else result
        return
    else:
        for i in range(idx,26):
            if not alpha[i]:
                alpha[i]=True
                gotoantatica(idx+1,cnt-1)
                alpha[i]=False
        
n,k=map(int,input().split())

max_result=0

if k==26 or k<5:
    print(0 if k<5 else n)
    exit(0)
    
l=[set(input().rstrip()) for _ in range(n)]    
alpha=[False]*26

for i in ('a','n','t','c','i'):
    alpha[ord(i)-ord('a')]=True
    
gotoantatica(0,k-5)

print(max_result)

from sys import stdin,exit
input=stdin.readline
def gotoanartica(index,k):
    global max_result
    if k==0:
        result=0
        for word in words:
            for w in word:
                if not alpha[ord(w)-ord('a')]:
                    break
            else:
                result+=1
        max_result=max(result,max_result) if max_result else result
        return
    for i in range(index,26):
        if not alpha[i]:
            alpha[i]=True
            gotoanartica(i+1,k-1)
            alpha[i]=False
            
N,K=map(int,input().split())
words=[]
max_result=0
if K<5 or K==26:
    print(0 if K<5 else N)
    exit(0)
words=[set(input().rstrip()) for _ in range(N)]

alpha=[False]*26
for i in ('a','n','t','i','c'):
    alpha[ord(i)-ord('a')]=True
gotoanartica(0,K-5)
# 리스트로 묶인 집합모음 words
# 리스트로 묶인 알파벳 부울 모음 alpha
print(max_result)

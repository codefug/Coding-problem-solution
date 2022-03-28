#10809 알파벳 찾기

s=input()

alpha=[-1 for i in range(26)]

for i in range(len(s)):
    if alpha[ord(s[i])-97]==-1:
        alpha[ord(s[i])-97]=i
        
for i in alpha:
    print(i,end=' ')
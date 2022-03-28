#1181 단어 정렬

n=int(input())

word=[]

for _ in range(n):
    
    w=input()
    
    if word.count((len(w),w))==0:
        
        word.append((len(w),w))

word.sort()

for number,w in word:
    print(w)
#10814 나이순 정렬

n=int(input())

l=[]

for i in range(n):
    
    old,name=input().split()

    l.append([int(old),name])
    
l.sort(key=lambda x:x[0])

for set in l:
        
    print(set[0],set[1])
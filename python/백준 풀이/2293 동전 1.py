#acmicpc.net/problem/2293 동전 1
n,k=map(int,input().split())

l=[]

for i in range(n):
    l.append(int(input()))
max_=0
def findanswer(l,k):
    global max_
    if k==0:
        max_+=1
    elif k<0:
        return
    else:
        for j in range(len(l)):
            findanswer(l,k-l[j])
findanswer(l,k)
print(max_)

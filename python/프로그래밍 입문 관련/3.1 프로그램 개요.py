N=int(input("리스트 원소의 개수N:"))
k=int(input("회전 단계수 k:"))
n=[]
for j in range(N):
    n.append(j+1)
print("원래 리스트:",n)
m=len(n)
for j in range(k):
    for i in range(m-1,0,-1):
        n[i],n[i-1]=n[i-1],n[i]
print("회전 회오리:",n)

    
    

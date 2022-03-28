#12865 평범한 배낭

#조건들이 존재한다. 1. 가방의 무게가 k보다 커지면 안되고 2. 물품의 수는 n이며 3. 각 물품당 가치가 정해져있다.
#4. 여기서 중요한건 같은 물건을 못 넣는다는 점 #5.

n,k=map(int,input().split())

weight=[]

value=[]

for i in range(n):
    
    w,v=map(int,input().split())

    weight.append(w)

    value.append(v)

dp=[[-1 for i in range(k+1)] for i in range(n+1)]

dp[0][0]=0


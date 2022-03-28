from sys import stdin
import heapq #힙으로 하나씩 넣다뺴기 해야댐 위상정렬

input=stdin.readline
push=heapq.heappush
pop=heapq.heappop

t=int(input()) #t 입력

for i in range(t): #테스트 케이스

    n,k=map(int,input().split()) #건물 갯수 n, 규칙 갯수 k입력

    time=[0]+[*map(int,input().split())] #각 건물의 소요 시간 인덱스=건물이름

    forward=[[] for i in range(n+1)] #앞으로 무슨 건물을 지을수있나

    hp=[] #힙

    beforecount=[0]*(n+1) #이거 지을려면 몇개 더 해결되야하나 인덱스 = 건물이름
    
    for i in range(k): #규칙 갯수 만큼 a,b로 받아서 

        a,b=map(int,input().split())

        forward[a].append(b) #a건물이면 b를 지을수 있다.
        
        beforecount[b]+=1 #b건물 지을려면 남은 카운트

    w=int(input()) #최종 건물

    t=[0]*(n+1) #dp 생성 작은 문제로 나눈건 이제 각 번호의 최소시간>모든 번호의 최소시간

    for i in range(1,n+1): #1부터 n까지

        if beforecount[i]==0: #무조건 된다면

            push(hp,i)

            t[i]=time[i]

            beforecount[i]-=1

    while hp:

        x=pop(hp)

        for y in forward[x]:

            beforecount[y]-=1

            if t[y] < t[x]+time[y] : t[y]=time[y]+t[x]

            if beforecount[y]==0 : push(hp,y)

    print(t[w])

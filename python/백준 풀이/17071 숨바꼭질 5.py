#17071 숨바꼭질 5 정리

'''
조건에 맞춰서 도는데 이제 조건이 뭐냐 하면
1. bfs 내에서 홀수와 짝수 로 구분을 하자면 이 전의 있던 홀수의 것은 이후에 홀수의 것에 다 포함된다. 고로 계속 홀수번쨰는 홀수 visited에 짝수번째는 짝수 visited에 탐색을 저장하다가
만약 지금 돌고 있는 curtime 이 이전에 탐색했었던 거라면 (홀 짝 맞춰서) 바로 현재 시간 출력 이걸 하기 위해서는 기존에 -1 +1 *2를 세부적으로 나누었던걸 안하고 전부 다 세어줘야함
'''
def f(n,k):

    visited=[[False]*500001 for i in range(2)]
    #0은 짝수 1은 홀수

    flag=0

    visited[flag][n]=True

    todo=[n]

    curtime=0

    while todo:

        nexttodo=[]

        if k>500000:

            return -1

        if visited[flag][k]==True:

            return curtime

        curtime+=1

        k+=curtime

        flag=flag^1

        for n in todo:

            for i in (n+1,n-1,n*2):

                if 0>i or i>500000:

                    continue

                if visited[flag][i]==False:

                    visited[flag][i]=True

                    nexttodo.append(i)

        todo=nexttodo

n,k=map(int,input().split())

time=f(n,k)

print(time)

    

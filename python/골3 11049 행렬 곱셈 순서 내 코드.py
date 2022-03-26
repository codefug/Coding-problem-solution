#11049 행렬 곱셈 순서 내 코드

n=int(input())

graph=[]

for i in range(n):
    
    graph.append(list(map(int,input().split())))
    
'''
dp에서 신경써야 할 것 두가지
1.시작점
2.끝점
'''

dp=[[0]*n for i in range(n)]

"""
점화식
dp[s][e]=min(dp[s][e],dp[s][k]+dp[k+1][e]+graph[s][0]*graph[k][1]*graph[x][1])

이건 솔직히 직접 손으로 풀어보는게 더 편할 수 있다 나 또한 그랬고 한국어인가 싶더라

일단 그래도 적어보자면 기본적으로 행렬의 곱셈은 두개의 행렬이 적어도 하나는 행과 열이 같아야 한다.
예를 들어 a 와 b 행렬이 있다고 했을때 a의 행이나 열은 b의 열이나 행과 같아야 한다는거다. a(q*w) b(w*e) 이런식이면 w가 a의 열과 b의 행에 둘다 있으니 곱셈 할 수 있는 것이다
이렇게 본다면 이 문제에서 순서대로 곱할 수 있다고 한걸로 보면 다른 건 몰라도 앞의 행과 뒤의 열은 같다는 걸 알 수 있다. 예제 입력 1 로 보자
3 
5 3 
3 2 
2 6
잘 보면 3 3 2 2 열 행 열 행 이렇게 같은걸 볼 수있다. 그렇다면 각각을 A B C행렬이라고 해보자
A 행렬 자체는 5*3이 될 것이다. A부터 B까지의 행렬은 ? 5*2 가 될거다. 행렬의 곱셈을 하게 되면 같은 행 렬 제외한걸로 만들어지기 때문이다.
이걸 코드로 짜면 graph[0][0]*graph[1][1] 이런 식이다. 만약 A부터 C까지라면? 5*6 이 되고 이는 graph[0][0]*graph[2][1] 이런식이다.
근데 우린 연산 수를 알아야 한다. 이게 중요한게 이때까지 우리가 한건 완성된 행렬이 어떤 형태인가를 알아본 것이였다.
연산의 수는 이 같은 것을 한번 곱해주는 것이다 예를 들면 A*B면 (a*b행렬)*(b*c행렬) 연산수는 a*b*c가 된다는 것이다.
여기서 우리가 생각해야 될 것은 A*B*C로 갔을때 A BC AB C 이렇게 두가지로 생각할 수 있다는 것이다. 이 두가지 경우의 연산 수가 왜 다른지는 손으로 직접 해보길 바란다.
이 두가지가 있으니 우린 반복문을 사용해야 한다는걸 생각해야 되고 연산수를 구할 때 그 직전까지 각각을 만들때 쓰여지는 연산 수 + 이 두개를 합칠 때의 연산수
를 DP로 쭈욱 구하면 답이 나온다는 생각이 들어야한다.
이를 위해 앞에서 했던 완성된 행렬이 어떤 형태인지 아는 방법을 사용한다.
그렇게 하면 
DP[시작][끝]=for문으로 돌릴 K값이 있는데 이 K값으로 나눠진 각각의 DP들(여기서 DP는 시작부터 끝까지 다 해봤을때 최소의 연산수) + DP가 나왔으니 이 두 행렬을 합치는 연산수
이런식으로 생각하면 된다.
다시 말하자면 손으로 한번 풀어보는게 훨씬 쉽다. 나도 힘들었다. ㅠㅠ
"""
'''
점화식 구하셈
'''

for i in range(1,n):
    for j in range(n-i):
        x=i+j
        dp[j][x]=2**32
        for k in range(j,x):
            dp[j][x]=min(dp[j][x],dp[j][k]+dp[k+1][x]+graph[j][0]*graph[k][1]*graph[x][1])
print(dp[0][n-1])

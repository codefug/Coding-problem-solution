import sys

input = sys.stdin.readline
#스탠다드 인풋

INF = int(1e10)
#최댓값 설정

T = int(input())
#테스트 케이스 입력

for t in range(T):
#테스트 케이스

    N = int(input())
#n입력

    file = [0] + list(map(int, input().split()))
#파일 리스트

    sum_file = file
#초기 파일 부분합

    for i in range(1, N):

        sum_file[i+1] += sum_file[i]
#i=인덱스 i-1까지 다 합친 값

    K = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        K[i][i] = i
#i부터 i까지할때 k를 중간점으로 나눴을때 최소가 될때 그 k값

    dp = [[0] * (N+1) for _ in range(N+2)]
#dp 설정

    for i in range(1, N):
#파일의 크기 차이

        for j in range(1, N-i+1):
#처음 파일

            dp[j][i+j] = INF
# 갱신 환경

            for k in range(K[j][i+j-1], K[j+1][i+j]+1):
# 크누스 알고리즘

                temp = dp[j][k] + dp[k+1][i+j] + sum_file[i+j] - sum_file[j-1]
# 점화식

                if temp < dp[j][i+j]:
# 점화식이 최솟값보다 작으면

                    dp[j][i+j] = temp
# 최솟값 갱신

                    K[j][i+j] = k
# k값 갱신

    print(dp[1][N])
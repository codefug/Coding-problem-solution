import sys

read = sys.stdin.readline
# 스탠다드 인풋

MAX = sys.maxsize
# 최댓값

def solution(N, A):
# solution 함수

    sums = [0]
# 부분합 함수

    for i in A:

        sums.append(sums[-1] + i)
# 부분합 함수 완성 sums[i]=A[i]까지 더한 값

    dp = [[], [0] * N, [sums[i + 2] - sums[i] for i in range(N - 1)]]
# dp=[[?][?][ i는 A[i+1] A[i] 합친 값 ]

    knuth_old = [1] * (N - 1)
# Knuth_old=[1,1,1]

    for d in range(3, N + 1):
# d는 ?

        min_sum, knuth_new = [], []
# min_sum=최솟값 , knuth_new=갱신할 값

        for i in range(N - d + 1):
        #d와 합치면 N이 되서 최댓값 안 넘게 함
        
            tmp_sum, tmp_knuth = MAX, knuth_old[i]
            #현재값, 현재 크누스 = 최댓값(갱신위해), 이전 크누스[i?]
            
            for k in range(knuth_old[i], knuth_old[i + 1] + 2):
            #k는 knuth_old[i]부터 knuth_old[i+1]+2 까지
                          
                if tmp_sum >= (new_sum := dp[k][i] + dp[d - k][k + i] + sums[d + i] - sums[i]):
                # 현재값이 새로운 값(A[i]부터 A[i+d]의 값의 합과 dp[k][i] dp[d-k][k+i]?)
                    
                    tmp_sum, tmp_knuth = new_sum, k
                    # 현재값, 현재 크누스 = 새로운 값, k
            
            min_sum.append(tmp_sum)
            # 최솟값에 현재값 추가
            
            knuth_new.append(tmp_knuth)
            # 새로운 크누스는 현재 크누스
        
        dp.append(min_sum)

        knuth_old = knuth_new
        #예전 크누스 갱신
        
    return dp[-1][-1]


if __name__ == '__main__':

    T = int(read())
#테스트 값 t
    for _ in range(T):
#테스트 케이스
        N = int(read())
#파일 개수
        A = list(map(int, read().split()))
#파일 리스트
        print(solution(N, A))
import sys
std_input = sys.stdin.readline
#stdin

k, n = map(int, std_input().split())
arr = [int(std_input()) for _ in range(k)]
#array 설정

def possible(length):
    cnt = 0
    for ll in arr:
        cnt += ll // length
    return cnt >= n
#랜선이 n개 이상 나오면 1 안나오면 0

st = 1
ed = 2**31 - 1
#시작값, 끝값

while st < ed:
    mid = (st+ed+1)//2
    if possible(mid):
        st = mid
    else:
        ed = mid-1
#시작값이 끝값보다 작으면 돌아라
#mid값은 시작값과 끝값의 중간이 된다.
#possible함수를 mid가 통과하면 시작값은 중간값이 되고
#끝값은 중간값 -1 값이 된다.

print(st)
#시작점 출력
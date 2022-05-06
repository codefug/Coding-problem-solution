#12969 ABC 답지

from collections import deque

N, K = map(int, input().split())
#n,k 입력

a= (N-1)//3+1

b = ((N-1)//3)+1 if N%3 != 1 else (N-1)//3

c = N - a - b

temp = (N//3-1)*2+1 if N%3 != 2 else (N//3-1)*2+2

arr = list('C'*c+'B'*b+'A'*a)

num = 0

for _ in range(K//(temp+1)):

    arr.insert(0, arr.pop())

    num += (temp+1)

    if arr[-1] == 'B':


        break

if num < K:

    b_idx = deque()

    for i in range(N):

        if arr[i] == 'B':

            b_idx.append(i)

    s = arr[b_idx[0]-1]

    while b_idx and num < K:

        B = b_idx.popleft()

        while num< K:

            if arr[B-1] != s:

                break

            arr[B], arr[B-1] = arr[B-1], arr[B]

            num += 1

            B = B-1

if num != K:

    print(-1)

else:

    print(''.join(arr))
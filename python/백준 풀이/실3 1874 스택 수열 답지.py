#1874 실3 스택 수열 답지

import sys

n = int(sys.stdin.readline())

stack = []

count = 0

result = [] # 43687521

no_message = True

for _ in range(n):

    k = int(sys.stdin.readline())
    
    while count < k:

        count += 1

        stack.append(count)

        result.append("+")
    
    if stack[-1] == k:

        stack.pop()

        result.append("-")

    else:

        no_message = False

        continue

if no_message == False:

    print("NO")

else:

    print("\n".join(result))
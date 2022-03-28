#1789 수들의 합 정리

import sys

from collections import defaultdict

input=sys.stdin.readline

def sum_of_the_numbers(s):

    dp=defaultdict(int)

    i=0

    while dp[i]<=s:

        i+=1

        dp[i]=dp[i-1]+i

    return i

if __name__=="__main__":

    s=int(input())

    max_number=0

    print(sum_of_the_numbers(s))

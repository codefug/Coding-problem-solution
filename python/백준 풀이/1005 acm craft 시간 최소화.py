import sys

from collections import defaultdict

input=sys.stdin.readline

t :"test case"

n:"the number of buildings"

k:"the number of construction order rules"

d:"time"

input=sys.stdin.readline

def get_times(i:int) -> int:

    if dp[i]!=-1:
        
        return dp[i]

    result=0

    for build in order[i]:

        result=max(result,get_times(build))

    dp[i]=result+d[i]

    return dp[i]

def main() -> None:

    global dp,order,d

    for t in range(int(input())):

        n,k=map(int,input().split())

        d=[0]+list(map(int,input().split()))

        order=defaultdict(list)

        for i in range(k):

            u,v=map(int,input().split())

            order[v].append(u)

        dp=[-1 for i in range(n+1)]

        print(get_times(int(input())))

if __name__ == "__main__":
    
    sys.setrecursionlimit(2000)

    main()

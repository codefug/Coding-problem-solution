# 10818 최소,최대 정리

n=int(input())

min_count=1000001

max_count=-1000001

l=list(map(int,input().split()))

for i in l:

    if i<min_count:

        min_count=i

    if i>max_count:

        max_count=i

print(min_count,max_count)

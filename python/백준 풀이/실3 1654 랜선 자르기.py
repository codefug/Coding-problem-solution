#1654 랜선 자르기

'''
1.k 랜선
2.n 랜선
3.최대 랜선의 길이
4.다 자르고 남으면 버림
'''

k,n=map(int,input().split())

line=[int(input()) for i in range(k)]

start,end=1,max(line)

while start<=end:
    mid=(start+end)//2
    answer=0
    for i in line:
        answer+=i//mid
    if answer>=n:
        start=mid+1
    else:
        end=mid-1
print(end)
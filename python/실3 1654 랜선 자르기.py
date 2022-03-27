#1654 랜선 자르기

'''
1.k개의 랜선 n개의 랜선 동일한 길이
2.n을 만들려고 k를 자르고 남으면 버림
3. 자르거나 만들때 손실 x
4. 무조껀 k개 만으로 n 만들 수 있음
5. n보다 많이 만들 수 있음
6. 만들 수 있는 최대 랜선의 길이
'''

k,n=map(int,input().split())

line=[int(input()) for i in range(k)]

start=0

end=max(line)

while start<=end:

    mid=(start+end)//2
    
    answer=0
    
    for i in line:
        
        answer+=i//mid
        
    if answer>=n:
        
        start=mid+1
        
    elif answer<n:
        
        end=mid-1
        
print(end)
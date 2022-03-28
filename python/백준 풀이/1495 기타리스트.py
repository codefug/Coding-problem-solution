#1495 기타리스트

import sys
input=sys.stdin.readline
#스탠다드 인풋

'''
곡의 개수 n 시작 볼륨 s 볼륨 제한 m
각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이 
'''
song_number,start_volume,limit_volume=map(int,input().split())
#곡 개수, 시작 볼륨, 볼륨 제한

volume_list=list(map(int,input().split()))
#볼륨 리스트

dp=[[0]*(limit_volume+1) for i in range(song_number+1)]
#dp 생성

dp[0][start_volume]=1
#dp 설정

for i in range(song_number):
    for j in range(limit_volume+1):
        if dp[i][j]==1:
            if j+volume_list[i]<=limit_volume:
                dp[i+1][j+volume_list[i]]=1
            if j-volume_list[i]>=0:
                dp[i+1][j-volume_list[i]]=1
#dp에 있는거 대로 i값은 곡의 개수 j는 최대 볼륨 리스트를 돌리는데
#이제 단계를 올린다고 생각하면 된다. 1일때 조건을 만족하면 다음 단계 1

ans=-1
#ans 생성

for m in range(limit_volume,-1,-1):
    if dp[song_number][m]:
        ans=m
        break
#마지막 리스트의 높은 순으로 쭉 내려가서 1이면 ans를 갱신하고 출력 없으면 그대로 끝나서 -1
    
print(ans)
#답

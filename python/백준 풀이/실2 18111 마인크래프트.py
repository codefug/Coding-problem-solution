#18111

from sys import stdin

input=stdin.readline

def solution():
    n,m,b=map(int,input().split())

    height_list=dict()

    for i in range(n):
        for j in map(int,input().split()):
            if j in height_list:
                height_list[j]+=1
            else:
                height_list[j]=1
                
    total_block=0
    '''
    기본적인 생각 돌리기 전에
    이제 인벤토리양이랑 블록양 신경 안쓰고 싶으면 
    총 블록 구해서 돌릴때 총블록 넘는거 안 구한다는 마인드
    돌리는건 i로 돌리는데 시간 단계로 끉어서 생각하는거랑 같다고 보면 된다.
    높이로 끉어서 최소값일때 리턴
    '''
    for i in height_list:
        total_block+=i*height_list[i]
    
    max_height=0
    min_time=1001*n*m
    
    for i in range(257):
        
        if n*m*i <= total_block+b:

            time=0
            
            for block in height_list.keys():
                if block<i:
                    time+=(i-block)*height_list[block]
                else:
                    time+=(block-i)*2*height_list[block]
        
            if time<=min_time:
                
                min_time=time
                
                max_height=i
                
    print(min_time,max_height)
                
if __name__=='__main__':
    solution()
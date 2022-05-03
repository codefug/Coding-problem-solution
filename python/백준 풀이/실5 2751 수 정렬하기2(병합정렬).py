#실5 2751 수 정렬하기2 (병합정렬)

from sys import stdin

input=stdin.readline

'''

1. 리스트 요소 1개만 남을때까지 리스트 쪼개고

2. 쪼갠 바로 그 다음에 두개를 비교해준다.

3. 거기서 작은 순서대로 넣고 리턴

4. 리턴 된걸 다시 비교

5. 재귀

6. 완성
'''
n=int(input())
#n 입력

l=[]
#리스트

for i in range(n):
    
    l.append(int(input()))
#l 입력

def merge_sort(l):
    
    if len(l)<=1:
        
        return l
    
    mid=(len(l)//2)
    
    left=l[:mid]
    
    right=l[mid:]
    
    left=merge_sort(left)
    
    right=merge_sort(right)
    
    return merge(left,right)
#재귀 중 중간에 merge를 갔다가 옴으로써 에러가 뜨지 않고 리스트가
#정상적으로 출력됨 왼쪽 오른쪽을 나눈후 그 나눈걸 다시 나누고
#1이 되었을때 그것을 출력하는 함수
 
def merge(left,right):
    
    l=r=0
    
    answer=[]
    
    while l<len(left) and r<len(right):
        
        if left[l]<right[r]:
            
            answer.append(left[l])
            
            l+=1
            
        else:
            
            answer.append(right[r])
            
            r+=1
            
    answer+=left[l:]
    
    answer+=right[r:]
    
    return answer

for i in merge_sort(l):
    
    print(i)
# 주어진 왼쪽 오른쪽을 순서대로 놓는 함수 이후 출력
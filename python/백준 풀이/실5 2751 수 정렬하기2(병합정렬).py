#실5 2751 수 정렬하기2 (병합정렬)
'''
1. 리스트 요소 1개만 남을때까지 리스트 쪼개고
2. 쪼갠 바로 그 다음에 두개를 비교해준다.
3. 거기서 작은 순서대로 넣고 리턴
4. 리턴 된걸 다시 비교
5. 재귀
6. 완성
'''
n=int(input())
list=[]
answer=[]

def solve(l):
    
    if len(l)<=1:
        return l
    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]
    left=solve(left)
    right=solve(right)
    return go(left,right)

def go(left,right):
    answer=[]
    l=r=0
    while l<len(left) and r<len(right):
        if (left[l]<right[r]):
            answer.append(left[l])
        else:
            answer.append(right[r])      
    answer.append(left[l:])
    answer.append(right[r:])
    return answer
    
for i in range(n):
    list.append(int(input()))

answer=solve(list)

for i in answer:
    
    print(i)
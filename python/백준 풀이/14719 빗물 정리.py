#14719 빗물 정리

h,w=map(int,input().split())
#height:h width:w

block=list(map(int,input().split()))
#the list of arranged block

long=max(block)
#the largest number of blocks

ans= h*w - sum(block)
#we first need to know the total area minus the number of blocks.

if long != h:

    ans-=(h-long) * w
#if miximum height is smaller than the largest number of blocks we need to subtract h minus long multiplied by c from ans


for i in range(w):

    if block[i]==long:

        l=i

        break

for j in range(w-1,-1,-1):

    if block[j]==long:

        r=j

        break
    
#we need to find index values for the largest number of blocks on both sides.

l_index=l
r_index=r

l_max=long
r_max=long

#store each index value and maximum value.

while l_index>0:

    l_sub_block=block[:l]
    l_sub_max=max(l_sub_block)
    for i in range(l-1,-1,-1):
        if block[i]==l_sub_max:
            index=i
            break
    ans-=(l_max - l_sub_max)*l
    if index==0:
        break
    l=index
    l_max=l_sub_max

while r_index < w-1:

    r_sub_block=block[r+1:]
    r_sub_max=max(r_sub_block)
    for i in range(r+1,w):
        if block[i]==r_sub_max:
            index=i
            break
    ans-=(r-max - r_sub_max) * (w-1-r)
    if index==w-1:
        break
    r=index
    r_max=r_sub_max
print(ans)

# firstly we got the width of the block at its maximum height and we also got index values and maximum values for the largest number of blocks on both sides.
# now we should subtract blocks from the width with idea of cutting the height by little and little
# find the highest value except i for each direction and store its index value and that value
# and if that value is not in other lower(l) index value find the number of l_max minus l_sub_max
# subtract that number multiplied by l_index minus l_sub_index from total area from 0 to l_index
# if that value is in other lower index change l_max and l to l_sub_max and l_sub_index
# ans would be the answer

'''
h, w = map(int, input().split())
block = list(map(int, input().split()))

long = max(block)
ans = h * w - sum(block)

if long != h:
    ans -= (h - long) * w

# 가장 긴 벽의 위치 탐색
for i in range(w):
    if block[i] == long:
        l = i
        break
for j in range(w - 1, -1, -1):
    if block[j] == long:
        r = j
        break
# 왼쪽 큰 블럭의 인덱스와 오른쪽 큰 블럭의 인덱스를 따로 저장.        
l_index = l
r_index = r
# 왼쪽과 오른쪽의 블럭들의 최댓값을 long으로 지정.
l_max = long
r_max = long

# 왼쪽(처음에 가장 큰 블럭이 맨 왼쪽에 있으면 왼쪽을 볼 필요 없음.)
while l_index > 0:
    l_sub_block = block[:l]
    l_sub_max = max(l_sub_block)
    for i in range(l-1, -1, -1):
        if block[i] == l_sub_max:
            index = i
            break            
    ans -= (l_max - l_sub_max) * l
    if index == 0:
        break
    l = index
    l_max = l_sub_max
# 오른쪽(왼쪽과 마찬가지로 큰 블럭이 맨 오른쪽에 있으면 오른쪽을 볼 필요 없음.)
while r_index < w - 1:
    r_sub_block = block[r + 1:]
    r_sub_max = max(r_sub_block)
    for i in range(r + 1, w):
        if block[i] == r_sub_max:
            index = i
            break
    ans -= (r_max - r_sub_max) * (w - r - 1)
    if index == w - 1:
        break
    r = index
    r_max = r_sub_max
print(ans)
'''

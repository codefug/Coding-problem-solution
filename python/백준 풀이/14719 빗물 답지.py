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

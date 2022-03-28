#뮤탈리스크 이틀차

scv=int(input())

scv_order=list(map(int,input().split()))

while len(scv_order)!=3:

    scv_order.append(0)

dp=[[[61 for i in range(scv_order[2]+1)] for j in range(scv_order[1]+1)] for q in range(scv_order[0]+1)]


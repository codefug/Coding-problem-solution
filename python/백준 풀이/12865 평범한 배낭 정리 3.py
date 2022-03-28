#12865 평범한 배낭

import sys

input=sys.stdin.readline

n,k=map(int,input().split())

dp={0:0}

for i in range(n):

    w,v=map(int,input().split())

    tmp={}
    
    for dw,dv in dp.items():

        nw=dw+w;nv=dv+v

        if nw<=k and nv>d.get(nw,0):

            tmp[nw]=nv

    dp.update(tmp)

print(max(dp.values()))

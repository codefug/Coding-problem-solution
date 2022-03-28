n=int(input())
cnt_0=0
cnt_1=1
for i in range(n-1):
    if i%2:
        tmp_cnt_0=cnt_0+cnt_1-1
    else:
        tmp_cnt_0=cnt_0+cnt_1
    tmp_cnt_1=cnt_0+cnt_1
    cnt_0=tmp_cnt_0
    cnt_1=tmp_cnt_1
print(cnt_0)

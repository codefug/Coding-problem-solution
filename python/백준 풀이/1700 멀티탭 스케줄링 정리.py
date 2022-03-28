#1700 멀티탭 스케줄

n,k=int(input().split())

order=list(map(int,input().split()))

consent=[]

answer=0

for i in range(len(order)):

    if order[i] not in order[i+1:]:

        order[i]+=100



'''
while order:

    now_item=order.pop(0)

    if consent.count(now_item)==0 and len(consent)<n:

        consent.append(now_item)

    elif len(consent)==n and consent.count(now_item)==0:

        consent.remove(max(consent))

        consent.append(now_item)

        answer+=1
'''

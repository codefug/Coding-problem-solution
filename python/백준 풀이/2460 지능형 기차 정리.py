#2460 지능형 기차2 정리

train=0

max_people=0

for i in range(10):

    a,b=map(int,input().split())

    train+=(b-a)

    if train>max_people:

        max_people=train

print(max_people)

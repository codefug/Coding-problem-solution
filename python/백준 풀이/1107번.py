num=int(input())
m=int(input())
li=list(map(int,input().split()))
l=[i for i in range(10) if li.count(i)==0]
#남아있는 수 중에 가장 가까운수를 높은 자리 수부터 쭉 돌리고(중복 가능) n만큼 cnt+1

#두 수의 차 만큼 -클릭 즉 cnt+1

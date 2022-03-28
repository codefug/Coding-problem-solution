#16953 A - > B

'''
생각해야되는 점
1. A가 B를 넘으면 끝이다 줄어드는 경우는 없다.
2. 2로 곱하거나 1을 오른쪽에 추가하거나 두가지의 방법만 있다.
결론: 2가지를 사용하는 모든 경우의 수를 구하나 B를 넘는 순간 다른 것으로 바꾸는 것이 필요하며
이것의 시간을 줄이기 위해서는 dp의 도움이 필요할 것이다.
'''
def multi2(x):

    x*=2

    return x

def add1(x):

    x=str(x)

    x+="1"

    return int(x)

def bfs(x):

    global result
    
    queue=[[a,1]]

    while queue:

        num,count=queue.pop(0)

        if num>b:

            continue

        elif num==b:

            result= min(result,count)

        else:

            queue.append([multi2(num),count+1])

            queue.append([add1(num),count+1])
            
a,b=map(int,input().split())

result=10**9+1

bfs(a)

if result==10**9+1:

    print(-1)

else:

    print(result)

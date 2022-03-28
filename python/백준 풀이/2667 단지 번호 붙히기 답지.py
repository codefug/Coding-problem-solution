n=int(input()) #n값 입력

l=[] #l생성

dx=[0,0,1,-1] #상하좌우 x

dy=[1,-1,0,0] #상하좌우 y

for i in range(n): #n값으로 이중리스트로 입력
    
    l.append(list(input()))

cnt=0 #카운트

apt=[] #단지수 담을 리스트

def dfs(x,y): #재귀 함수 dfs

    global cnt #카운트 
    
    l[y][x]='0' #현재 x,y는 이미 1이니깐 0으로 바꿔줌

    cnt+=1 #현재 단지 카운트

    for i in range(4): #상하좌우 각각

        nx = dx[i] + x #현재값 + 상하좌우 x값

        ny = dy[i] + y #현재값 + 상하좌우 y값

        if nx < 0 or nx >= n or ny < 0 or ny >= n: #x,y가 범위를 넘어가면 넘어가고

            continue

        if l[ny][nx]=='1': #상하좌우중 하나라도 1이면 재귀
            
            dfs(nx,ny)

for i in range(n):
    for j in range(n): #모든 좌표 1인지 확인
        if l[i][j]=='1':
            cnt=0 #cnt 단지마다 0 초기화
            dfs(j,i)
            apt.append(cnt) #단지수 apt 입력

            
print(len(apt)) #단지수의 수는 단지의 개수
apt.sort() #정렬시키고
for i in range(len(apt)):
    print(apt[i]) #단지수 출력

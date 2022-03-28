#14226 이모티콘

def bfs(s):

    queue=[(0,1)]
#인덱스 0이 클립보드 1이 스크린

    curtime=0
    
    while True:

        nextqueue=[]

        for i in queue:
            
            clip,scr=i

            if scr==s:

                return curtime

            if clip!=0 and clip+scr<=s and visited[clip][scr+clip]==False:

                visited[clip][scr+clip]=1
                
                nextqueue.append((clip,clip+scr))

            if scr!=0 and visited[clip][scr-1]==False:

                visited[clip][scr-1]=1

                nextqueue.append((clip,scr-1))

            if scr!=0 and visited[scr][scr]==False:

                visited[scr][scr]=1

                nextqueue.append((scr,scr))

        curtime+=1
        
        queue=nextqueue

s=int(input())

clipboard=0

screen=1

visited=[[0]*1001 for i in range(1001)]

print(bfs(s))

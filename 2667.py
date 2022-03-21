from collections import deque

N = int(input())
graph = []
counts = []

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(x,y):
    graph[x][y] = 0
    count = 1
    
    #여기를 꼭 이런식으로 하기 
    queue = deque()
    queue.append((x,y))



    while queue:
        x, y = queue.popleft()
        
        #방향 상하좌우
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        #방향 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #갈 수 있는곳이면 graph[dx][dy] == 1
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    count += 1
                
    #한개 단지 끝나면 append
    counts.append(count)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i,j)


counts.sort()
print(len(counts))

for i in counts:
    print(i)

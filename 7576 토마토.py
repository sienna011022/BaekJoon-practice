from collections import deque


M,N = map(int,input().split())
visited = [[0]*(M) for _ in range(N)]
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))
res = 0
queue= deque()
for i in range(M):
    for j in range(N):
        if graph[j][i] == 1:
                queue.append((j,i))

def bfs():
    while queue:
        x,y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                #visited 행렬에 -1도 표시해줘야지 0으로 인식안함
                if graph[nx][ny] ==0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx,ny))


bfs()

for i in graph:
    #graph원소 탐색
    for j in i:
        #다 익히지 못함
        if j == 0:
            print(-1)
            exit(0)
    #다익혔다면 최대값이 정답
    res = max(res, max(i))

print(res-1)


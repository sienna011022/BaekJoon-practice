from collections import deque

N,M = map(int,input().split())
visited = [[0]*M for _ in range(N)]

graph = []
for i in range(N):
    graph.append(list(map(int,input())))





def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[0][0] = 1


    while queue:
        x, y = queue.popleft()

        if x == N - 1 and ny == M - 1:
            print(visited[x][y])
            break
        for i in range(4):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            nx = x + dx[i]
            ny = y + dy[i]




            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))








bfs(0,0)















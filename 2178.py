from collections import deque

N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
print(graph)




def bfs(x,y):

    graph[0][0] = 0
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        dy = [-1,1,0,0]
        dx = [0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                if nx == N-1 and ny == M-1:
                    return

            #이동코드
                graph[nx][ny] = graph[x][y] + 1
                print(graph[nx][ny])
                queue.append((nx,ny))











bfs(0,0)
print(count)

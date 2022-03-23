
from collections import deque

def bfs(i,j):
    graph[i][j] = 0
    queue = deque()
    queue.append((i,j))



    while queue :
        x,y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))



    # 한개 단지 끝나면 append
    counts.append(count)


T = int(input())


for i in range(T):
    counts = []
    count = 0
    N,M,K = map(int,input().split())
    graph = [[0] *(M+1) for _ in range(N+1)]

    for _ in range(K):
        a,b = map(int,input().split())
        graph[a][b] = 1





    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                #여기서 count올라기기
               count += 1
    print(len(counts))







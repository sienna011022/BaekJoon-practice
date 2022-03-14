N = int(input())
M = int(input())

matrix = [[0] *(N+1) for _ in range(N+1)]
visited_list = [0]*(N+1)

#전역 변수 처리해주기
global count
count = 0

for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1



def bfs(V):
    visited_list[V] = 1
    global count
    #인덱스 조심하기
    for i in range(N+1):
        if visited_list[i] == 0  and matrix[V][i] == 1:
            bfs(i)
            #더해주는 위치도 중요함
            count += 1
bfs(1)
print(count)
n,m,v = map(int,input().split())
#리스트 인덱스 0을 없애기 위함.
graph = [[] for _ in range (1)]

for i in range(m):
    first,end = map(int,input().split())
    graph.append([first,end])
print(graph)
visited = [False] * m
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    #그 안을 탐색 [1,2]면 1을 탐색
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)




from collections import deque
N,M,V = map(int,input().split())

#이차원 행렬을 정의한다.
matrix = [[0] * (N+1) for i in range(N+1)]

#연결된 노드들을 1로 표시한다
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a]=1

#확인용 visit_list정의
visit_list1 = [0] * (N + 1)
visit_list2 = [0] * (N + 1)

def dfs(V):
    visit_list1[V] = 1
    print(V,end=' ')
    for i in range(1,N+1):
        #방문기록이 없고 V와 인접하는 경우 재귀
        if(visit_list1[i] == 0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):
    #queue에 V를 넣어 첫번쨰 원소는 미리 넣어두기
    queue = deque([V])
    #첫번째꺼는 수동으로 설정
    visit_list2[V] = 1
    #이 아래는 while문이라서 맨 마지막에 visit_list[i]=1을 해줘야함.
    while queue:
        #queue에 들어있는 첫번쨰 원소를 뽑는다 없애는 상태.
        V = queue.popleft()
        print(V,end= ' ')
        #여기서 V와 인접한 모든 원소를 탐색하게됨
        for i in range(1,N+1):
            if(visit_list2[i] == 0 and matrix[V][i] == 1):
                queue.append(i)
                visit_list2[i] = 1
dfs(V)
print(' ')
bfs(V)

graph = [(1,2,13),(1,3,5),(2,4,9),(3,4,15),(3,5,3),(4,5,1),(4,6,7),(5,6,2)]


graph.sort(key=lambda x:x[2])

mst =[]
n = 6
p = [0]
#루트 저장 or 부모노드 저장
for i in range(1,n+1):
    p.append(i)

#루트
def find(u):
    if u!= p[u]:
        p[u] = find(p[u])
    return p[u]

#두개의 집합을 하나로 합침
def union(u,v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1


tree_edges = 0
mst_cost = 0

while True:
    if tree_edges == n-1:
        break
    u,v,wt = graph.pop()
    if find(u) != find(v):
        union(u,v)
        mst.append((u,v))
        mst_cost += wt
        tree_edges += 1
print("최소신장트리",mst)
print("최소 신장 트리 가중치",mst_cost)

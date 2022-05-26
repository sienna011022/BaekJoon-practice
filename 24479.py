
from collections import  deque
from sys import stdin

node,edge,start = map(int,stdin.readline().split())

adj = [[]for _ in range(node+1)]
visited_list = [False] * (node+1)
visited_list[0] = True
line = [0]*(node+1)


for _ in range(edge):
    src,dest = map(int,stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)

for i in adj:
    #pop을 쓸것이기에 역정렬을 해주어야 맨 마지막 값이 가장 작은 값이 된다.
    i.sort(reverse = True)

stack = deque()
stack.append(start)
count = 1
while stack:
    cur_node = stack.pop()

    visited_list[cur_node] = True
    if line[cur_node] == 0:
        #값을 넣는 것이 아닌 순서를 넣는 것이기 때문에 cnt라는 값을 증가시켜야함
        line[cur_node] = count
        count += 1

    for next_node in adj[cur_node]:
        if not visited_list[next_node]:
            stack.append(next_node)



for i in line[1:]:
    print(i)

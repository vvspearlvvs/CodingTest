#BFS2
#연결된 그래프를 []형식으로 표현
#큐를 그냥 list로 표현
import sys
from collections import deque
input=sys.stdin.readline

node = int(input())
line = int(input())

graph=[[0]*(node+1) for _ in range(node+1)]
for _ in range(line):
    a, b = map(int,input().split())
    graph[a][b]=graph[b][a]=1
print(graph)
# 연결되면1, 연결안되면0으로 표현한 그래프
#[
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 1, 0, 0, 1, 0, 0],
#    [0, 1, 0, 1, 0, 1, 0, 0],
#    [0, 0, 1, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 1],
#    [0, 1, 1, 0, 0, 0, 1, 0],
#    [0, 0, 0, 0, 0, 1, 0, 0],
#    [0, 0, 0, 0, 1, 0, 0, 0]
#]
def bfs(graph,start):
    visited=[start]
    queue=deque()
    queue.append(start)
    #print(queue)
    while queue:
        v=queue.popleft()
        #print(v)
        for w in range(len(graph[v])):
            if graph[v][w]==1 and w not in visited:
                visited.append(w)
                queue.append(w)
                #print(visited)
            #else:
                #print("이미방문")
    return visited
print(len(bfs(graph,1))-1)

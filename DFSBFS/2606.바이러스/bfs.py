#BFS
#연결된 그래프를 {}형식으로 표현
#큐를 그냥 list로 표현
import sys
input=sys.stdin.readline

node = int(input())
line = int(input())
graph={}
for i in range(node):
    graph[i+1] = set()
for j in range(line):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
print(graph)
# {노드:{연결된 노드들}}
#{1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}

def bfs(start,dic):
    #print("##bfs시작")
    queue=[start]
    #print(queue)
    while queue:
        v=queue.pop()
        #print(v)
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
            #    print(visited)
            #else:
            #    print("이미방문")
    return visited
visited=[]
print(len(bfs(1,graph))-1)

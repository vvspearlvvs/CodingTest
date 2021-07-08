#BFS -큐(deque)이용
import collections import deque
#각 노드가 연결된 정보 표현
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

def bfs(graph,start,visited):
    #현재노드 방문처리
    queue=deque([start])
    visited[start]=True

    while queue:
        #큐에서 하나의 원소 뽑아
        v=queue.popleft()
        print(v,end=' ')
        #아직 방문하지 않은 인접한 노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

print("##최종")
bfs(graph,1,visited)

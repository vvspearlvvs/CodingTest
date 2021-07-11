#DFS-stack이용
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

def dfs(graph,v,visited):
    #현재노드 방문처리
    visited[v]=True
    prnit(v,end=' ')
    #현재노드와 연결된 다른노드를 재귀적으로 밤문
    for i in graph[v]:
        if not in visited[i]:
            dfs(graph,i,visited)

print("##최종")
dfs(graph,1,visited)

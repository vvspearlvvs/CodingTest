def dfs(graph, v, visited): #graph:전체리스트, v: index, visited: 방문여부 체크
    if visited[v] ==0
        visited[v] ==1 # 방문처리

    #DFS수행
    for e in range(len(graph)):
        if computer[v][e]==1 and visited[e]==0:
            dfs(graph, e, visited)

def solution(n, computers):
    count = 0
    visited = [0] * n

    while 0 in visited:
        for i in range(n):
            # 새로운 네트워크가 시작되는 경우(False일경우)
            if visited[i] ==0:
                dfs(computers, i, visited)
                count += 1 #방문계산
    return count

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
#방문할 수 있는 곳을 모두 방문하고,
#방문하지 않은 곳이 있으면 다시 dfs호출

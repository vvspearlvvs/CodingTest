node,line,start=map(int,input().split())
print(node,line,start)
graph=[[0]*(node+1) for _ in range(node+1)]

for j in range(line):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
print(graph)
 

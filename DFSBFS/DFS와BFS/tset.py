'''
input
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
n,m,v=map(int,input().split())
s=[[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]


def dfs(v):
  visit[v]=1 #방문완료 체크
  print(v, end='') #1243
  for i in range(1,n+1):
    #방문완료는 아직 아니면서,이어져있을떄
    if visit[i] ==0 and s[v][i]==1:
      dfs(i)

def bfs(v):
  queue = [v]
  visit[v] = 0 #방문완료 체크
  while queue:
    v= queue.pop(0)
    print(v,end='') #1234
    for i in range(1,n+1):
      #방문완료로 이어져있는 값일때
       if visit[i] ==1 and s[v][i]==1:
         queue.append(i)
         visit[i]=0

for i in range(m):
  x,y=map(int,input().split())
  s[x][y]=1
  s[y][x]=1

print(s)
# 0 0 0 0 0
# 0 0 1 1 1
# 0 1 0 0 1
# 0 1 0 0 1
# 0 1 1 1 0

print("##dfs")
dfs(v)
print("##bfs")
bfs(v)

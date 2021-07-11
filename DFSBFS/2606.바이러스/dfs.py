#DFS
#연결된 그래프를 {}형식으로 표현

import sys
input=sys.stdin.readline
node = int(input())
line = int(input())
dic={}
for i in range(node):
    dic[i+1] = set()
for j in range(line):
    a, b = map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)
print(dic)
# {노드:{연결된 노드들}}
#{1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}

def dfs(start,dic):
    #print("dfs시작")
    #print(dic[start])
    for i in dic[start]:
        #print(i)
        if i not in vistited:
            vistited.append(i)
            #print(vistited)
            dfs(i,dic)
        else:
            print("이미방문")

vistited=[]
dfs(1,dic)
print(len(vistited)-1)

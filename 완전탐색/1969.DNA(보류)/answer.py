import sys
input=sys.stdin.readline

n,k=map(int,input().split())
dna_list=[]
for i in range(n):
    dna_list.append(input())
word=''
dist=0

for i in range(n):
    dict={}
    for j in range(n):
        if dna_list[i][j] not in dict:
            dict[dna_list[i][j]] =1
        else:
            dict[dna_list[i][j]] +=1
    print(dict)
    ans = list(dict.items())
    ans.sort(key=lambda x: (-x[1],x[0]))
    print(ans)
    word +=ans[0][0]
    dist +=n-ans[0][1]
print(word)
print(dist)

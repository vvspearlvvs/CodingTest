from collections import defaultdict
import sys
input=sys.stdin.readline

n=int(input())
dic=defaultdict(int)

for _ in range(n):
    file=input().rstrip().split(".")[1]
    dic[file]+=1

sort_dict= sorted(dic.items())
print(sort_dict)
for i in sort_dict:
    print(i[0],i[1])

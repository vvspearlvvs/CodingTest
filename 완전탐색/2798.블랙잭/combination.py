#combinations 사용 : 메모리 29200KB, 시간120mx
from itertools import combinations
n,m=map(int,input().split())
arr=list(map(int,input().split()))

MAX=0
for c in combinations(arr,3):
    comb_sum = sum(c)
    if comb_sum<=m and comb_sum>MAX:
        MAX=comb_sum
print(MAX)

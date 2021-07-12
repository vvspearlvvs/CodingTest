
import sys
from collections import Counter

input=sys.stdin.readline
n=int(input())
arr=list(int(input()) for _ in range(n))
#print(arr)

#산술평균
print(round(sum(arr)/len(arr)))
#중앙값
print(sorted(arr)[n//2])
#최빈값
count_order=Counter(arr).most_common() #[(-1, 2), (-2, 2), (-3, 1)]
max=count_order[0][1]
modes=[]
for i in count_order:
    if i[1]==max:
        modes.append(i[0])
sorted_modes = sorted(modes)
if len(sorted_modes)>1:
    print(sorted_modes[1])
else:
    print(sorted_modes[0])

'''
dic={}
for i in arr:
    dic[i]=dic.get(i,0)+1
print(dic) #{-1: 2, -2: 2, -3: 1}
'''
#범위
arr.sort()
print(arr[-1]-arr[0])

from functools import cmp_to_key  # cmp_to_key가 필요한 경우 import
import sys
n= int(sys.stdin.readline())
num=[]
for _ in range(n):
    a,b= map(int,sys.stdin.readline().split())
    num.append((a,b))
#print(num)
def xy_compare(a, b):
    if a[1] > b[1]: # y좌표가 작은 것부터 앞으로 가게 정렬
        return 1
    elif a[1] == b[1]: # y좌표가 같을 경우
        if a[0] > b[0]: # x 좌표가 작은 것부터 앞으로 가게 정렬
            return 1
        elif a[0] < b[0]: # x 좌표가 큰 것은 뒤로 가게
            return -1
        else: # 같은 경우에는 그대로
            return 0
    else: # y좌표가 큰 것이 뒤로 가게
        return -1

num = sorted(num, key=cmp_to_key(xy_compare))
#print(num)
for i in num:
    print(i[0],i[1])

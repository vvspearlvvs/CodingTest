#dict사용 : 메모리 50352, 시간 240ms
import sys
input=sys.stdin.readline
n=int(input().rstrip())
n_list=list(map(int,input().split()))

n_dict={}
for val in n_list:
    n_dict[val]=1
#print(n_dict)

m=int(input())
m_list=list(map(int,input().split()))
for val in m_list:
    try:
        print(n_dict[val])
    except KeyError:
        print(0)

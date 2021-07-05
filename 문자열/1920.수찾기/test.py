#시간초과.in검색
import sys
input=sys.stdin.readline
n=int(input())
n_list=list(map(int,input().split()))

m=int(input())
m_list=list(map(int,input().split()))

for m in m_list:
    if m in n_list:
        print("1")
    else:
        print("0")

#출력초과.
import re
import sys
input=sys.stdin.readline
n=int(input())
n_list=''.join(input().split())

m=int(input())
m_list=''.join(input().split())
for m in m_list:
    if re.search(m,n_list):
        print("1")
    else:
        print("0")

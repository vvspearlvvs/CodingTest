
#이진탐색 : 메모리 44724KB, 시간 916ms
import sys
input=sys.stdin.readline

n=int(input())
n_list=list(map(int,input().split()))
n_list=sorted(n_list)

m=int(input())
m_list=list(map(int,input().split()))

def binary_search(element,some_list,start=0,end=None):
    if end==None:
        end=len(some_list)-1
    if start>end:
        return 0

    mid = (start+end) //2

    if element == some_list[mid]:
        return 1
    elif element < some_list[mid]:
        end = mid-1
    elif element > some_list[mid]:
        start = mid+1
    return binary_search(element,some_list,start,end)

for i in range(len(m_list)):
    print(binary_search(m_list[i],n_list))

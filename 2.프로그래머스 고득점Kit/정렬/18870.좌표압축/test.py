import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
#dic={arr_sort[i]:i for i in range(len(arr_sort))}
dic={num:i for i,num in enumerate(sorted(set(arr)))}
#print(dic)

for i in arr:
    if i in dic.keys():
        print(dic[i],end=' ')

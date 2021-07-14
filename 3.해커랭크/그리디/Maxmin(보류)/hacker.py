#arr' : k길이의 unfariness가 최소화인 arr들의 elements 모임
#max(arr')-min(arr')=?
#unfariness?

def maxMin(k, arr):
    diff_list=[]
    arr_sort=sorted(arr)
    unfair=0
    print(arr_sort)

    for i in range(len(arr_sort)-1):
        diff_list.append(arr_sort[i+1]-arr_sort[i])
    print(diff_list)

    for i in range(k-1):
        unfair+=diff_list[i]
    min=unfair
    print(unfair)
    '''
    for i in range(k-1,len(diff_list)):
        unfair-=diff[i-(k-1)]
        unfair+=diff[i]
        if min>unfair:
            min=unfair

    print(min)
    '''


n = int(input().strip())
k = int(input().strip())
arr = []
for _ in range(n):
    arr_item = int(input().strip())
    arr.append(arr_item)
maxMin(k, arr)

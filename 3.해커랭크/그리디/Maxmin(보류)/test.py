def maxMin(k,arr):
    diff_list=[]
    arr_sort=sorted(arr)
    print("sort",arr_sort)
    diff = abs(arr_sort[0]-arr_sort[1])

    for i in range(len(arr_sort)-1):
        newdiff=arr_sort[i+1]-arr_sort[i]
        print(newdiff)
        if diff>=newdiff:
            diff=newdiff
            diff_list.append(arr_sort[i])
    return len(diff_list)


n = int(input().strip())
k = int(input().strip())
arr = []
for _ in range(n):
    arr_item = int(input().strip())
    arr.append(arr_item)
maxMin(k, arr)

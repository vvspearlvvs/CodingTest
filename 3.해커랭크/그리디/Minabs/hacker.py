#시간초과
def minimumAbsoluteDifference(arr):
    #print(arr)
    abs_list=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            abs_list.append(abs(arr[i]-arr[j]))
    #print(abs_list)
    return min(abs_list)

#정답
def minimumAbsoluteDifference2(arr):

    arr_sort=sorted(arr)
    diff = abs(arr_sort[0]-arr_sort[1])

    for i in range(len(arr_sort)-1):
        newdiff=abs(arr_sort[i]-arr_sort[i+1])
        if diff>newdiff:
            diff=newdiff
    return diff


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
#min=minimumAbsoluteDifference(arr)
#print(min)
min=minimumAbsoluteDifference2(arr)
print(min)

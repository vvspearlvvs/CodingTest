#sort사용한 방법 : 1초
def miniMaxSum(arr):
    # Write your code here
    result=[]
    arr=sorted(arr)
    result.append(sum(arr[0:4]))

    arr2=sorted(arr,reverse=True)
    result.append(sum(arr2[0:4]))

    for i in result:
        print(i,end=' ')


#combination사용한 방법 :5초
from itertools import combinations
def miniMaxSum(arr):
    result=[]
    combi=combinations(arr,4)
    for c in combi:
        result.append(sum(c))
    print(min(result),max(result))


arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)

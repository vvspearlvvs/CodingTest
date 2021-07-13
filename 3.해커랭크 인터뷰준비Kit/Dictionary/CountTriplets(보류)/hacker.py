#세쌍의 지수를 구하시오
#[1,4,16,64] r=4일때
#지수가 되는 값 : 1,4,15 또는 4,16,64
#이들의 위치 : (0,1,2) 또는 (1,2,3) = 2리턴

from collections import defaultdict
def countTriplets(arr, r):
    dict=defaultdict(int)
    dictpairs=defaultdict(int) #지수가 되는 값 일치하는 것
    count=0
    for i in arr:
        count+=dictpairs[i]
        dictpairs[i*r]+=dict[i]
        dict[i*r]+=1
    print(count)


nr = input().rstrip().split()
n =int(nr[0]) #list size
r =int(nr[1]) #r
arr = list(map(int, input().rstrip().split()))
ans = countTriplets(arr, r)


#4 2
#1 2 2 4

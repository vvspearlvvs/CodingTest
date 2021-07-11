def solution(a, b):
    tmp=0
    for i in range(len(a)):
        tmp=tmp+a[i]*b[i]
    return tmp


print(solution([1,2,3,4],[-3,-1,0,2])) #3
print(solution([-1,0,1],[1,0,-1])) #-2

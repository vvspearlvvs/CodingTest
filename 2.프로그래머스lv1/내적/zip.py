def solution(a,b):
    tmp=[]
    for x,y in zip(a,b):
        tmp.append(x*y)
    return sum(tmp)

print(solution([1,2,3,4],[-3,-1,0,2])) #3
print(solution([-1,0,1],[1,0,-1])) #-2

'''
zip사용하기
https://www.daleseo.com/python-zip/
'''

def solution(n, m):
    answer = []
    while m!=0:
        (n,m)=(m,n%m)
    return answer


print(solution(3,12))
print(solution(2,5))

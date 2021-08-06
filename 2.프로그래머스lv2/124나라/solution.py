def solution(n):
    num=['1','2','4']
    if n<=3:
        return num[n-1]
    else:
        q,r=divmod(n-1,3)
        print("몫",q," 나머지",r)
        return solution(q)+num[r]

print(solution(6))

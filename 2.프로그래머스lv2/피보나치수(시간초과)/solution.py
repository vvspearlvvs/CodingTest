#재귀-시간초과
def pivot(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (pivot(n-1)+pivot(n-2))%1234567
#print(pivot(5))

#동적계획법
def solution(n):
    answer = [0,1]
    if n<2:
        return answer[n]
    else:
        for i in range(2,n+1):
            pivot=answer[i-1]+answer[i-2]
            answer.append(pivot)
        return answer[n]

print(solution(5))

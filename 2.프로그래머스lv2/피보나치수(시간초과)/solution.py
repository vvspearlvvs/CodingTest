#재귀-시간초과
def pivot(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (pivot(n-1)+pivot(n-2))%1234567
#print(pivot(5))

def solution(n):
    answer = []
    for i in range(n+1):
        if i==0 or i ==1:
            answer.append(i)
        else:
            pivot=answer[i-1]+answer[i-2]
            answer.append(pivot%124567)
    return answer[-1]
print(solution(5))

n=int(input())

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

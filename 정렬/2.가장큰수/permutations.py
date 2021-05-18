from itertools import permutations

def solution(numbers):
    answer =[]
    for i in permutations(numbers,len(numbers)):
        k=''.join(list(map(str,i)))
        answer.append(k)
    return max(answer)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
#시간초과로 실패

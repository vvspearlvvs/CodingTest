from itertools import combinations

def solution(numbers):
    answer = set()
    for a in combinations(numbers,2):
        answer.add(sum(a))
    return sorted(answer)

print(solution([2,1,3,4,1]))

'''
새로배운것
combinations
'''

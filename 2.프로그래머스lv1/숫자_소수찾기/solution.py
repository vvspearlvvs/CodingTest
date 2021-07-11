import math

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    for i in range(1,numbers+1):
        if check(i):
            answer+=1
    return answer

print(solution(10))

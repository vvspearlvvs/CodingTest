#진법함수 안쓰고 풀기

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3) #나머지 이어붙이면서 3진수 만듬
        n = n // 3

    answer = int(tmp, 3)
    return answer

print(solution(45)) #7
print(solution(125)) #229

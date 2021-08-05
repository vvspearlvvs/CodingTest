#조건1. answer은 n보다 큰 자연수
#조건2. answer와 n을 2진수로 변환했을때 1의 개수가 같다
#조건3. anwer은 조건1과 조건2를 만족하는 가장작은수
def solution(n):
    binary = bin(n)
    onecnt = str(binary).count('1')
    while True:
        n=n+1
        if bin(n).count('1') == onecnt:
            break
    return n
print(solution(78))


#for문 풀이
'''
def solution(n):
    binary = bin(n)
    onecnt = str(binary).count('1')
    for i in range(n+1,10000001):
        if bin(i).count('1') == onecnt:
            return i
'''

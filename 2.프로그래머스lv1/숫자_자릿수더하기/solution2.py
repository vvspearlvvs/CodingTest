def solution(number):
    if number < 10:
            return number;
    return (number % 10) + solution(number//10)

print(solution(123)) #6

'''
다른풀이: 재귀함수 사용
N의 범위가 100,000,000 이하의 자연수 이지만
재귀함수를 쓰면 max제한을 직접 언급하지 않아도 된다!
'''

def solution(a, b):
    answer = 0
    if a<b:
        for i in range(a,b+1):
            answer +=i
    elif a>=b:
        for i in range(b,a+1):
            answer +=i
    return answer

'''
간단풀이
if a > b: a, b = b, a
return sum(range(a,b+1))
'''

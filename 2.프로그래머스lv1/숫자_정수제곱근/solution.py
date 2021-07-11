import math
def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return math.pow(math.sqrt(n)+1,2)
    else:
        return -1

print(solution(121)) #144
print(solution(3)) #144

'''
제곱(n의2승) : math.pow(n,2)
루트(루트n값) :math.sqrt(n)
루트값이 양수인지 math.sqrt(n) == int(math.sqrt(n))
'''

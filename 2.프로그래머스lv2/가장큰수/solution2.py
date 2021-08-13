#큰수를 기준으로 정렬이 되어야한다.
#문자열 A+B로 만든 숫자와 B+A로 만든 숫자를 비교해서 큰수 확인하고 정렬
#cmp_to_key()사용

from functools import cmp_to_key

def mycmp(A,B):
    sA=str(A)
    sB=str(B)
    if sA+sB < sB+sA:
        return 1 #큰수를 기준으로 정렬
    else:
        return -1

def solution(numbers):
    numbers.sort(key=cmp_to_key(mycmp))
    numbers=list(map(str,numbers))
    if numbers[0] == '0': #마지막테스트케이스
        return "0"
    return ''.join(numbers)

numbers=[6,10,2]  #6210
numbers2=[3, 30, 34, 5, 9] #9534330
print(solution(numbers2))

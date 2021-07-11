def solution(a, b):
    answer = ''
    day =['THU','FRI','SAT','SUN','MON','TUE','WED']
    mon = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    tmp = (sum(mon[:a-1])+b)%7
    answer = day[tmp]
    return answer

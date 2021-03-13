import datetime

def solution(a, b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    index = datetime.datetime(2016,a,b).weekday()
    answer = day[index]
    return answer

print(solution(5,24))

def solution(brown,yellow):
    s= brown+yellow
    for a in range(s,2,-1):
        if s%a == 0:
            b=s//a
            if yellow == (a-2)*(b-2):
                return [a,b]

print(solution(10,2))

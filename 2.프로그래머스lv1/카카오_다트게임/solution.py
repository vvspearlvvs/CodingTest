def solution(dartResult):
    answer = 0
    score=[]
    for i,num in enumerate(dartResult,1):
        if num =="S":
            score[-1] **=1
        elif num =="D":
            score[-1] **=2
        elif num =="T":
            score[-1] **=3
        elif num =="*":
            score[-1] *=2
            if len(score)>=2:
                score[-1] *=2
        elif num =="#":
            score[-1] *=-1
        else: #0~10 숫자
            if dartResult[i-1:i+1]=='10':
                score.append(10)
            elif dartResult[i-2:i] !='10':
                score.append(int(num))

    return sum(score)

print(solution('1S2D*3T'))

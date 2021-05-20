def solution(progresses, speeds):
    answer = []
    day=[]
    for p,s in zip(progresses,speeds):
        tmp=(100-p)//s
        if (100-p)%s !=0:
            tmp+=1
        day.append(tmp)
    print(day)

    front = 0
    for i in range(len(day)):
        if day[i]>day[front]:
            answer.append(i-front)
            front = i
    answer.append((len(day)-front))

    return answer

print(solution([93, 30, 55],[1, 30, 5]))
#print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

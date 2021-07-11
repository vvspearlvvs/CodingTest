def solution2(progresses, speeds):
    answer = []
    day=[]
    for p,s in zip(progresses,speeds):
        tmp=(100-p)//s
        if (100-p)%s !=0:
            tmp+=1
        day.append(tmp)
    print(day)

    count=1
    for i in range(len(day)):
        try:
            if day[i]<day[i+1]:
                answer.append(count)
                count=1
            else:
                day[i+1]=day[i]
                count+=1
        except IndexError:
            answer.append(count)

    return answer

print(solution2([93, 30, 55],[1, 30, 5]))
#print(solution2([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

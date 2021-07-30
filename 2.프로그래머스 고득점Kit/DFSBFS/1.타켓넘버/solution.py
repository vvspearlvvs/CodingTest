def solution(numbers, target):
    super = [0]
    for i in numbers:
        sub=[]
        for j in super:
            sub.append(j+i)
            sub.append(j-i)
        #반복하기 위해 다시
        super=sub
    return super.count(target)

numbers=[1,1,1,1,1]
target=3
print(solution(numbers, target))

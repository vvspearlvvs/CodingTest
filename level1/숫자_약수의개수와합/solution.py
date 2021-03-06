def med(number): #약수의 개수 구하는 함수
    count = 0
    for i in range(1,number+1):
        if number%i ==0:
            count+=1
    return count

def solution(left, right):
    answer = 0
    for n in range(left,right+1):
        if med(n)%2 ==0:
            answer = answer +n
        elif med(n)%2 ==1:
            answer = answer -n
    return answer

print(solution(13,17)) #13 + 14 + 15 - 16 + 17 = 43

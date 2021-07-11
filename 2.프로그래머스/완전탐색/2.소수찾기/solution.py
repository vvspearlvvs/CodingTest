from itertools import permutations
def is_sosu(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):      # math를 사용하지 않고 (num//2)+1 까지로 설정
            if num%n == 0:
                return False
        return True

def solution(numbers):
    answer = 0
    pre_list =[]
    num_list = list(map(int,numbers))
    print(num_list)

    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            pre_list.append(''.join(j))
    pre_list = list(map(int,pre_list)) #0제거 : int
    pre_list = list(set(pre_list))

    for i in pre_list:
        if is_sosu(i):
            answer +=1
    return answer

print(solution("17")) #3
print(solution("011")) #2

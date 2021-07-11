from itertools import combinations

def is_sosu(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):      # math를 사용하지 않고 (num//2)+1 까지로 설정
            if num%n == 0:
                return False

        return True
def solution(nums):
    count =0
    for a in combinations(nums,3):
        if is_sosu(sum(a)):
            count+=1

    return count

print(solution([1,2,7,6,4])) #4
print(solution([1,2,3,4])) #1

'''
combination()
중복을 허용하지 않고, 순서대로 뽑을 때
print(combinaion(전체list,몇개))
소수구하기
소수구하는 함수에서 반복문범위 (num//2)+1
'''

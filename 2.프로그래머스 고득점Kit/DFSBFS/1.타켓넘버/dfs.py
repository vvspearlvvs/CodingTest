global answer
def dfs(num,i,n,target):
    answer=0
    if i == len(num):
        if n==target:
            return 1
        else:
            return 0
    answer+=dfs(num,i+1,n+num[i],target)
    answer+=dfs(num,i+1,n-num[i],target)
    return answer


def solution(numbers,target):
    answer = dfs(numbers,0,0,target)
    return answer

numbers=[1,1,1,1,1]
target=3
print(solution(numbers, target))

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k=command
        arr=list(sorted(array[i-1:j]))
        answer.append(arr[k-1])
    return answer


a=[1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,c))

def solution(array, commands):

    def com(arr,i,j,k):
        arr= arr[i-1:j]
        arr.sort()
        return arr[k-1]

    answer = []
    for i,j,k in commands:
        answer.append(com(array,i,j,k))

    return answer

a=[1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,c)) #[5, 6, 3]

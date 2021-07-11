def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        answer.append(bin(i|j)[2::].zfill(n).replace('1','#').replace('0',' '))
    return answer


arr1 =[3, 20, 28, 18, 11]
arr2 =[5, 1, 21, 17, 28]
print(solution(5,arr1,arr2))

#

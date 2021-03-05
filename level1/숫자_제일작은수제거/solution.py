def solution(arr):
    answer = []
    min = 1000

    if len(arr) == 1:
        answer.append(-1)
    else:
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]
        for i in arr:
            if min != i:
                answer.append(i)
            else:
                continue
    return answer

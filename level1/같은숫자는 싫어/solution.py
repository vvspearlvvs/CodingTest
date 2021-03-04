def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0: #새로운숫자는 무조건 추가
            answer.append(arr[i])
        elif arr[i] !=arr[i-1]: #그전과 다르면 이제 연속이 끝나서 추가
            answer.append(arr[i])
    return answer

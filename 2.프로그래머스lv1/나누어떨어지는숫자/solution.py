def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor ==0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return sorted(answer)

print(solution([5, 9, 7, 10],5)) #[5, 10]
print(solution([2, 36, 1, 3],1)) #[5, 10]
print(solution([3,2,6],10)) #[-1]

'''
한줄로 줄이면?
return sorted([i for i in arr if i%divisor ==0]) or [-1]
'''

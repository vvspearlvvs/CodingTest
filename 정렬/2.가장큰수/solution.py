def solution(numbers):
    answer = ''
    numbers= list(map(str,numbers)) # ['6', '10', '2']
    numbers.sort(key=lambda x:x*3,reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))
#print(solution([3, 30, 34, 5, 9]))

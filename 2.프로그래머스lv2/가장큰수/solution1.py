def solution(numbers):
    numbers = map(str,numbers)
    sort_numbers=sorted(numbers,key=lambda x:x*3,reverse=True)
    return str(int(''.join(sort_numbers)))

numbers=[6,10,2]
print(solution(numbers))

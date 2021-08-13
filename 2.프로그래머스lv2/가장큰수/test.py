from itertools import permutations
def solution(numbers):
    max=0
    result_list=[]
    numbers = list(map(str,numbers))
    numbers_list = list(permutations(numbers,len(numbers)))

    for num in numbers_list:
        result_list.append(''.join(num))
    result_list=list(map(int,result_list))
    for i in result_list:
        if i>max:
            max=i
    return str(max)

numbers=[6,10,2]  #6210
numbers2=[3, 30, 34, 5, 9] #9534330
print(solution(numbers2))

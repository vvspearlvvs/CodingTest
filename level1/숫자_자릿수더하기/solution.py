def solution(n):
    list_int=map(int,str(n)) #[1, 2, 3]
    return sum(list_int)

print(solution(123)) #6


'''
참고
문제는 input이 int라서 int->str->list_int로 map
만약 input이 str이였다면 str->list_int로 map

list_str = list(s)
list_int = list(map(int,list(n))) #[1, 2, 3]
'''

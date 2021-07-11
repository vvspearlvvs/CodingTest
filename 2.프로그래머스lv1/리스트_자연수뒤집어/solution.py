def solution(n):
    answer = []
    num_list = list(map(int,str(n)))
    answer = list(reversed(num_list))
    return answer

    #return list(map(int,reversed(str(n))))

print(solution(12345)) #[5,4,3,2,1]

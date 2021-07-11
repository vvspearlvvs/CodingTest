def solution(participant, completion):
    answer = ''
    check=dict()
    for i in participant:
        check[i]=check.get(i,0)+1
    for i in completion:
        check[i]=check.get(i,0)-1

    for key,value in check.items():
        if value !=0:
            answer = ''.join(key)
    return answer

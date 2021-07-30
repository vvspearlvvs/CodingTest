def solution(participant, completion):
    answer = ''
    check=dict()
    for i in participant:
        check[i]=check.get(i,0)+1
    for i in completion:
        check[i]=check.get(i,0)-1
    print(check)
    for key,value in check.items():
        if value !=0:
            answer = ''.join(key)
    return answer
participant2=["mislav", "stanko", "mislav", "ana"]
completion2=["stanko", "ana", "mislav"]
print(solution(participant2, completion2))

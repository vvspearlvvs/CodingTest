from collections import Counter
def solution(participant, completion):
    pcounter=Counter(participant)
    #print(pcounter)
    ccounter=Counter(completion)
    #print(ccounter)

    #counter끼리 -하면 중복되는 key끼리 value빼기 수행
    answer = pcounter-ccounter
    print(answer)
    return ''.join(answer.keys())


participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]
print(solution(participant, completion))

#예외사항 : 동명이인이 있을 경
participant2=["mislav", "stanko", "mislav", "ana"]
completion2=["stanko", "ana", "mislav"]
print(solution(participant2, completion2))

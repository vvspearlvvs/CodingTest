#binary gap :양끝이 1로 둘러싼 연속적인 0의 최대 시퀀스
#ex:9->1001
def solution(N):
    a=bin(N)[2::]
    if a.count('1') == 1 or a.count('0') == 0 :
        return 0

    maxlist=[]

    for i in range(len(a)):
        if a[i] == '1':
            cnt=0
        if a[i] =='0':
            cnt+=1
            maxlist.append(cnt)

    return max(maxlist)

#print(solution(9)) #1001 -> 길이 2개
#print(solution(145)) # 10010001 -> 길이 2,3
#print(solution(529)) #1000010001 -> 길이 4,3
#print(solution(20)) #10100 -> 길이 1
#print(solution(15)) #1111 -> 없음 (0)
print(solution(32)) #100000 -> 없음 (0)
#print(solution(1041)) #100000 -> 없음 (0)

def solution(N):
    bin_num = bin(N)[2::]
    cnt=0
    max=0
    for i in bin_num:
        if i=='1':
            if max < cnt:
                max = cnt
            cnt=0
        else:
            cnt+=1
    return max

print(solution(145)) # 10010001 -> 길이 2,3 ->3
print(solution(529)) #1000010001 -> 길이 4,3 ->4

print(solution(15)) #1111 -> 없음 (0)
print(solution(32)) #100000 -> 없음 (0)

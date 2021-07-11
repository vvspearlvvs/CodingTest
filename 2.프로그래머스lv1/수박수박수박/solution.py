def solution(n):
    answer = ''
    for i in range(n):
        if i %2 ==0:
            answer =answer +'S'
        elif i%2 ==1:
            answer = answer+'B'
    return answer

print(solution(3)) #SBS
print(solution(4)) #SBSB

'''
발상의전환.그냥 짜르면되잖아?
s='SB'*n
return s[:n]
'''

def solution(s):
    answer = ''
    alist=list(map(int,s.split()))
    answer = str(min(alist))+" "+str(max(alist))
    return answer

s="1 2 3 4"
print(solution(s))

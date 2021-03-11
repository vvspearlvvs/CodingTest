def solution(s):
    answer = ''
    tmp=sorted(list(s),reverse=True)
    answer = "".join(tmp)
    return answer

print(solution("Zbcdefg")) #"gfedcbZ"

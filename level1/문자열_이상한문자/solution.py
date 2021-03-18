def solution(s):
    answer = ''
    s_split = s.split(" ")
    for word in s_split:
        for i in range(len(word)):
            if i%2==0:
                answer+=word[i].upper()
            elif i%2==1:
                answer+=word[i].lower()
        answer+=' '
    return answer[:-1]

print(solution("try hello world")) #"TrY HeLlO WoRlD"
print(solution("apple orange")) #"TrY HeLlO WoRlD"


'''
맨끝 공백제거 : list[:-1]
리스트역순 : list[::-1]
'''

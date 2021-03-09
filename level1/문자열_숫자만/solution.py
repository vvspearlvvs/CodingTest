def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
    else:
        answer = False
    return answer
'''
간단풀이
return  s.isdigit() and len(s) in (4, 6)

#숫자만 있는지 확인 : s.isdigit()
#문자만 있는지 확인 : s.isalpha()
'''

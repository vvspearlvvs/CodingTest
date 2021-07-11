import re
def solution(new_id):
    answer = ''

    #1단계 : 모든대문자->소문자치환
    answer = new_id.lower()
    #2단계 : 알파벳소문자,-,_,.제외한 모든문자 제거
    answer = re.sub('[^a-z\d\-\_\.]','',answer)
    #3단계 : 2번이상 연속된 . -> 하나로 치환
    answer = re.sub('\.\.+','.',answer)
    #4단계 : .가 처음이나 끝에 있으면 제거
    answer = re.sub('^\.|\.$','',answer)
    #5단계 : 빈문자열이면 a대입
    if answer == '': answer = 'a'
    #6단계 : 길이가 16자 이상이면 1~15자만 남기기, 맨끝 . 제거
    answer = re.sub('\.$','',answer[0:15])
    #7단게: 길이가3이 될때까지 반복해서 끝에 붙이기
    while len(answer)<3:
        answer +=answer[-1:]
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))

'''
새로배운것
정규표현식 regular(import re) :
'''

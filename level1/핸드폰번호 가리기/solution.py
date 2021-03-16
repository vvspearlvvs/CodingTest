def solution(phone_number):
    answer = ''
    num = (len(phone_number)-4) *'*'
    back = phone_number[-4:]
    answer = num + back

    return answer

print(solution("01033334444")) #"*******4444"

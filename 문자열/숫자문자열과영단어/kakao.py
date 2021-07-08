def solution(s):
    dict={} #치환할 값
    en=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        dict[en[i]]=i
    print(dict)
    #{'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    result='' #최종 치환문자열
    eng=''
    for i in s: #문자열 하나씩 확인
        if i.isdigit(): #숫자면 그대로
            result=result+i
        elif i.isalpha(): #문자면 치환작업
            eng=eng+i #하나씩 이어붙임
            if eng in dict.keys(): #이어붙이다가 숫자단어가 되면
                result=result+str(dict[eng]) #dict에서 찾아서 치환
                eng=''
    return int(result)
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

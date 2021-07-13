#문장s가 입력될떄 사용된 단어의 개수를 구하시오
#첫번째 단어는 소문자로 시작되고, 그다음부터 대문자로 시작되는게 단어

#아이디어 : 대문자의개수+1 = 총 단어의 개수
def camelcase(s):
    count=0
    for i in s:
        if i.isupper():
            count+=1
    return count+1

s = input()
result = camelcase(s)

#input : saveChangesInTheEditor
#ouput : 5

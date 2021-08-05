#JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
def solution(s):
    return s.title()
    answer=''
    words = []
    for word in s.split(' '):
        word = word.capitalize()
        words.append(word)
    return ' '.join(words)

print(solution("3people unFollowed me"))
print(solution("for the last week"))

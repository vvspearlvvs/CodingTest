#모든문자가 알파벳(a-z)으로 구성되어 있는지 확인

#아이디어 : 중복을 제거해서 알파벳숫자(26)개인지 확인, 공백까지 포함해서 27개인지 확인
def pangrams(s):
    s=s.lower()
    s=set(s)
    s=list(s)
    #s.sort()
    if len(s) !=27:
        return "not pangram"
    else:
        return "pangram"


s="We promptly judged antique ivory buckles for the next prize"
result=pangrams(s) #다 있음
print(result)
s2="We promptly judged antique ivory buckles for the prize"
result2=pangrams(s2) #x가 없어서 not
print(result2)

#요구사항
#모든문자가 알파벳(a-z)으로 구성되어 있는지 확인

def pangrams(s):
    s=s.lower()
    s=set(s)
    s=list(s)
    s.sort()
    if len(s) !=27:
        return "not pangram"
    else:
        return "pangram"


s="We promptly judged antique ivory buckles for the next prize"
result=pangrams(s) #다 있음

s2="We promptly judged antique ivory buckles for the prize"
result2=pangrams(s2) #x가 없어서 not

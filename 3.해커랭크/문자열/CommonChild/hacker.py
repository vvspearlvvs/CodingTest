#요구사항
#두 문자 사이에 공통된 문자가 몇개인지 출력
def commonChild(s1,s2):
    s1=sorted(list(s1))
    s2=sorted(list(s2))
    print(set(s1))
    print(set(s2))

s1=input()
s2=input()
result=commonChild(s1,s2)

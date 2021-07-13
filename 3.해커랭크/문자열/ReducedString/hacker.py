#요구사항
#인접한 문자열들끼리 지운다
#aab -> aa붙어있어서 삭제 -> b
#abba ->bb붙어있어서 삭제 -> aa붙어있어서 삭제
def superReducedString(s):
    stack=[]
    result=''
    for i in range(len(s)):
        if len(stack)==0 or stack[-1]!=s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    if not stack:
        result="Empty String"
    else:
        result=''.join(stack)
    return result

s = input() #aaba
result = superReducedString(s)
print(result)

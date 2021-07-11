#시간초과
def hackerrankInString(s):
    findstr="hackerrank"
    strcount=0
    for i in range(len(s)):
        if findstr[strcount]==s[i]:
            strcount=strcount+1
    if len(findstr)==strcount:
        return "YES"
    else:
        return "NO"



q = int(input().strip())
for q_itr in range(q):
    s = input()
    result = hackerrankInString(s)

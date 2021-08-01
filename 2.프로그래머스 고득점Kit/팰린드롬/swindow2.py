#가장 긴 팰린드롬의 문자 출력
#가장 긴 팰린드롬의 길이 -> 13,18번줄 len으로 변경

def longestPalindrome(s):

    def expand(left,right):
        while (left>=0 and right<len(s)) and s[left]==s[right]:
            left-=1 #될때까지 계속 슬라이딩윈도우 이동
            right+=1
        return s[left+1:right]

    if len(s)<2 or s==s[::-1]: #길이가 한개이거나, 팰린드롬
        return s

    result="" #슬라이딩윈도우
    for i in range(len(s)-1):
        result = max(result,expand(i,i+1),expand(i,i+2),key=len)
    return result

print(longestPalindrome("abcdcba")) #가장긴 팰린드롬 : abcdcba -> len:3
print(longestPalindrome("abacde")) #가장긴 팰린드롬 : aba -> len :3

#가장 긴 팰린드롬 구하기 (대소문자구별)

#팰린드롬인가?
#가장긴가?
def longestPalindrome(s):
    maxLen=0 #최대길이인지 확인
    ans="" #슬라이딩윈도우

    for i in range(len(s)):
        #팰린드롬이 홀수일때
        left,right=i,i
        #팰린드롬인가?
        while (left>=0 and right<len(s)) and s[left]==s[right]:
            if maxLen<right-left+1: #슬라이딩윈도우 크기가 최대인가?
                maxLen=right-left+1
                ans=s[left:right+1] #윈도우 안에 있는 값
            left-=1 #될때까지 계속 슬라이딩윈도우 이동
            right+=1

        #팰린드롬이 짝수일때
        left,right=i,i+1
        while (left>=0 and right<len(s)) and s[left]==s[right]:
            if maxLen<right-left+1:
                maxLen=right-left+1
                ans=s[left:right+1]
            left-=1
            right+=1

    return ans

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))

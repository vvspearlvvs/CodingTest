#가장 긴 팰린드롬 길이 구하기 (대소문자구별)

from collections import Counter
def longestPalindrome(s):
    answer=0
    count=Counter(s)
    print(count)
    for value in count.values():
        answer += value //2 *2
        if answer %2 ==0 and value %2 ==1:
            answer+=1
    return answer


print(longestPalindrome("abccccdd")) #cc
print(longestPalindrome("abcccdd"))

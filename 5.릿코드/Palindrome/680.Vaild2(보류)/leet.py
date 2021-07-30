#적어도 한번 문자열을 제거한 후에 palindrome(팰린드롬)인지
from collections import Counter

def validPalindrome(str):
    answer = ''
    if str == str[::-1]:
        answer= true
        break
    else:
        count=Counter(str)
        for key,value in count.items():
            if value == 1:
                del count[key]
        answer = false

print(validPalindrome("aba")) #true
print(validPalindrome("abca")) #c제거 ->true
print(validPalindrome("abc"))  #false

# palindrome(팰린드롬)인가?

def isPalindrome(str):
    newstring=''
    for s in str:
        if s.isalnum(): #특수문자,공백 제거
            newstring+=s
    newstring=newstring.lower()

    return newstring==newstring[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

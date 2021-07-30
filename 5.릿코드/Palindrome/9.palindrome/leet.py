# palindrome(팰린드롬):거꾸로 읽어도 제대로 읽는 것과 같은 문장

def isPalindrome(n):
    string=str(n)
    if string == string[::-1]:
        return True
    return False

n=121
print(isPalindrome(n))

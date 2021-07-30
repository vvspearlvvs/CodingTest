#적어도 한번 문자열을 제거한 후에 palindrome(팰린드롬)인지
#투포인터(양끝)

def validPalindrome(s):
    left,right=0,len(s)-1
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            #팰린드롬이 안되는 문자열 제거
            tmp1=s[:left]+s[left+1:]
            tmp2=s[:right]+s[right+1:]
            print(tmp1,tmp2)

            #제거하고나서 팰린드롬인지
            return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
    return True


#print(validPalindrome("aba")) #true
print(validPalindrome("abca")) #c제거 ->true
print(validPalindrome("abc"))  #false

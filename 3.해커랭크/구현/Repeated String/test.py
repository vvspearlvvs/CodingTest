#시간초과, 단순하게 문자열 '하나씩' 이어붙이는 방법
s = input()
n = int(input().strip())
def repeatedString(s,n):
  substring=''
  while len(substring)<n:
      for i in range(len(s)):
          substring=substring+s[i]
          if len(substring) == n:
              break;
  return substring.count('a')
print(repeatedString(s,n))

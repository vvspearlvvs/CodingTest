'''
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
'''
# 문자열전체를 이어붙이고, n만큼 자르는 방법
s = input()
n = int(input().strip())
def repeatedString(s,n):
  substring=''
  while len(s)!=1:
      if len(s)==1 and 'a' in s:
          return n
      substring=substring+s
      if len(substring)> n:
          substring = substring[0:n]
          return substring.count('a')

print("##")
print(repeatedString(s,n))
#방법1. 문자열을 다 만들고 센다.
#방법2. 문자열을 만들면서 센다.

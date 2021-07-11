#시간초과, 문자열전체를 이어붙이고 n만큼 자르는 방법
# => 어차피 문자열 자르고 붙이는 방식이라 오래걸림
s = input()
n = int(input().strip())
def repeatedString(s,n):
  substring=''
  while True:
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

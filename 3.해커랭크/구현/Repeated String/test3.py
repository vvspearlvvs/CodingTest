#count말고, dict로 찾아보자.
s = input()
n = int(input().strip())
def counta(substring):
    count=0
    substring_dict={}
    for str in substring:
        if 'a' in str:
            count=count+1
            substring_dict[str]=count
    #print(substring_dict)
    return substring_dict['a']

def repeatedString(s,n):
  substring=''

  while True:
      if len(s)==1 and 'a' in s:
          answer=m
      elif len(s)==1 and 'a' not in s:
          answer = 0
      elif len(s)>n:
          substring = list(s[:n])
          #answer = substring.count('a')
          answer = counta(substring)
      else:
          answer =0
          loop_num = n//len(s)
          mod_num = n%len(s)
          s_a_count=counta(s)
          substring=list(s[:n])
          s_mod_count=counta(substring)
          answer = answer + (s_a_count*loop_num)+s_mod_count
      #print(substring)
      return answer

print("##")
print(repeatedString(s,n))

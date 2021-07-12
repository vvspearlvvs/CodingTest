#요구사항
#n이 주어졌을때,n개의 substring 중에서
#알파벳 'a'가 몇번나오는지

#직접 substring을 구하는게 아니라
#'갯수'에만 초점을 둬서 몫/나머지로 계산하기

s = input() #aba
n = int(input().strip()) #10
def repeatedString(s,n):
    if s.count('a')==0:
        return 0
    elif len(s)==1 and s=='a':
        return n
    else:
        s_count = s.count('a')
        m=int(n/len(s))
        remain_idx = int(n%len(s))
        remain=s[:remain_idx]
        return s_count *m + remain.count('a')

print(repeatedString(s,n))

#a부터z까지 문자열이 나타난 횟수 직접 count하는 방식
import sys
input=sys.stdin.readline
T=int(input())

for _ in range(T):
    sentence=input()

    max_alpha='' #가장 많이 나타나는 알파벳
    max_count=0 #가장 많이 나타나는 알파벳의 횟수

    #a부터 z까지 직접하나씩 몇개있는지 확인
    for j in range(ord('a'),ord('z')+1):
        cur_count=sentence.count(chr(j))
        #최대개수
        if cur_count>max_count:
            max_count=cur_count
            max_alpha=chr(j)
        elif cur_count==max_count:
            max_alpha="?"
        else:
            continue
    print(max_alpha)

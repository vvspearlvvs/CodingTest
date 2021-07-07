
#11781.그대로출력하기, #11719.그대로출력하기2
#특이사항 : sys.stdin.readline 하면 출력초
import sys
input = sys.stdin.readline
while True:
    try:
        print(input())
    except EOFError:
        break
#11721.열개씩 끊어서출력하기
n=input()
for i in range(0,len(n),10):
    print(n[i:i+10])

#2902.KMP.짧은형태 이름출력
import sys
input = sys.stdin.readline
words = input().rstrip()
word = words.split("-")
for w in word:
    print(w[0],end='')

import sys
input=sys.stdin.readline
str=input()
alpha='abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    print(str.find(i),end=' ')

#알파벳 선언하는 방법
#alpha='abcdefghijklmnopqrstuvxyz'
#alpha=list(map(chr,range(97,123)))

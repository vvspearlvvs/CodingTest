import sys
input=sys.stdin.readline
while True:
    n=input().rstrip()
    if n=="END":
        break
    print(n[::-1])

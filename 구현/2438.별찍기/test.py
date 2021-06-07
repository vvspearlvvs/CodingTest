#2438.별찍기1
'''
n=int(input())
for i in range(1,n+1):
    for _ in range(i):
        print("*",end='')
    print()
'''
#2439.별찍기2
n=int(input())
for i in range(1,n+1):
    for blank in range(n-i):
        print(" ",end='')
    for star in range(i):
        print("*",end='')
    print("")

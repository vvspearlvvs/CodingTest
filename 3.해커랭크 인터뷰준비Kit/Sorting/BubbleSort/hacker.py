def countSwaps(a):
    cnt=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] =a[j+1],a[j]
                cnt=cnt+1
    print("Array is sorted in {} swaps.".format(str(cnt)))
    print("First Element : ",a[0])
    print("Last Element : ",a[-1])
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
countSwaps(a)

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
a = list(map(int, input().rstrip().split()))

for i in range(len(a)):
    for j in range(i+1,len(a)):
        a[i]=a[j]
print(a)

for i in range(d):
    for j in range(len(a)):
        if i==0:
            tmp=a[i]
        else:
            a[i-1]=a[j]
    a[len(a)-1] = tmp
print(a)

from collections import Counter


n=int(input())
alist=[input().split(".")[1] for _ in range(n)]
#print(alist) #['txt', 'spc', 'icpc', 'icpc', 'txt', 'world', 'spc', 'txt']

count = Counter(alist)
count= sorted(count.items(),key=lambda x:x[0])
for i in count:
    print(i[0],i[1])

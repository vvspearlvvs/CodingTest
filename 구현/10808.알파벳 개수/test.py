#A-Z직접입력
n=input()
ALPHA='abcdefghijklmnopqrstuvxyz'
for a in ALPHA:
    print(n.count(a),end=' ')

#string 모듈사용하는 방법 (메모리:33048, 시간:152ms)
import string
n=input()
ALPHA=string.ascii_lowercase
for a in ALPHA:
    print(n.count(a),end=' ')

#collection 모듈사용하는 방법 (메모리:32040, 시간:96ms)
from collections import Counter
n=input()
alpha='abcdefghijklmnopqrstuvxyz'
dic=dict(Counter(n))

result = []
for i in alphabet_list:
    if i in dic:
        result.append(dic[i])
    else:
        result.append(0)

for i in range(len(result)):
    if i == len(result)-1:
        print(result[i])
    else:
        print(result[i], end = ' ')

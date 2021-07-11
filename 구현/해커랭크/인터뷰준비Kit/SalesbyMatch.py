n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
#ar.sort()
#print(ar)
#print(set(ar))
count_dict={}
for key in set(ar):
    count_dict[key]=ar.count(key)
print(count_dict)

result =0
for value in count_dict.values():
    if value>=2:
        result=result+value//2
print(result)
#하나씩 비교하는 방법
#count를 세는 방법 ->2로 나눈값

#10 20 20 10 10 30 50 10 20

#정렬하면 5.526
#정렬안하면 2.762

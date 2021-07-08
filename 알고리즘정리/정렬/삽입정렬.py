#삽입정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]: #한칸씩 왼쪽으로 이동
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
    print(arr)
print("최종")
print(arr)

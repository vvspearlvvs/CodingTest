#ㅔpassing cars count
# (p,q) p가 동쪽으로, q는 왼쪽으로 이동
# 0인 항목의 오른쪽에 있는 1의 수를 구해서 모두더함
# [0,1,0,1] -> 오른쪽1의 수를 세에서가면서 누적합

# 0의 개수를 누적해서 더하고, 1을 만나면 누적값을 result에 합산
def solution(A):
    result =0
    count_zero =0
    for i in A:
        if i==1 and count_zero ==0:
            continue
        elif i==0:
            count_zero +=1
        elif i==1:
            result+=count_zero

    if result>1000000000:
        return -1
    return result

A=[0,1,0,1,1]
print(solution(A))

input_num=int(input())
new=0
count=0

n=input_num #초기화한 변수(n),최종비교변수(input_num)이랑 다름
while True:
    sum = n//10 + n%10 #각 자리수더함
    new = (n%10)*10 + sum%10 #새로만들어지는 수
    count = count+1
    n=new

    if new==input_num:
        break

print(count)

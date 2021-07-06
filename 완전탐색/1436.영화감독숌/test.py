n=int(input())
cnt=0
num=1
while True:
    if "666" in str(num):
        cnt=cnt+1

    if cnt==n:
        print(num)
        break

    num=num+1


#tip: 'str' object is not callable
#변수명을 str로 지어서 str()을 사용하지 못함

#1666,2666..5666,6660,6661,6662...이렇게 가야한다..!

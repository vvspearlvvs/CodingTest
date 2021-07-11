#숫자로 쪼개고
#숫자앞에 0이 있는건 안됌
#연속적인숫자 (i,i-1의 차이가 1인것)
#연속된 숫자면 Yes,가장 작은 수 출력
#연속된 숫자가 아니면 No

def separatedNumbers(s):
    for i in range(1,len(s)+1):
        if 
        if abs(int(s[i])-int(s[i-1]))==1:
            print(s[i-1])


print(separatedNumbers("91011"))

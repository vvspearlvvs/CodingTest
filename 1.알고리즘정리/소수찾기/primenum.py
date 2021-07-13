#1.기존의 소수찾기
def is_prime_number(x):
    #2부터 x-1까지 '모든 수'를 확인
    for i in range(2,x):
        #x가 해당수로 나누어 떨어지면
        if x%i ==0:
            return False #소수가 아님
    return True #소수
print(is_prime_number(4)) #False
print(is_prime_number(7)) #True
print("#########")

#2.약수찾기를 이용한 소수찾기
import math

def is_prime_number2(x):
    #2부터 x의 제곱근까지 확인
    for i in range(2,int(math.sqrt(x))+1):
        #x가 해당수로 나누어 떨어지면
        if x%i ==0:
            return False #소수가 아님
    return True #소수
print(is_prime_number2(4)) #False
print(is_prime_number2(16)) #True
print("#########")

#3.에라토스테네스의 체 알고리즘을 이용한 소수찾기
import math
def is_prime_number3(x):
    array=[True for i in range(x+1)] #모든수 'True(소수)'로 초기화

    #2부터 x의 제곱근까지 확인
    for i in range(2,int(math.sqrt(x))+1):
        if array[i] == True: #i가 소수인경우 -> 남은수
            #i를 제외한 i의 모든 배수 지우기
            j=2
            while i*j<=n:
                array[i*j] = False #소수가 아님
                j+=1 #지울배수 찾기 위해 +1
    return array

n=10 #2부터 10까지 모든 수에 대하여 소수판별
sosu_array=is_prime_number3(n)
#모든 소출력
for i in range(2,n+1):
    if sosu_array[i]: #소수(True)일 경우
        print(i, end=' ')

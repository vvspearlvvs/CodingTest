keypad={
    1:(0,0),2:(0,1),3:(0,2),
    4:(1,0),5:(1,1),6:(1,2),
    7:(2,0),8:(2,1),9:(2,2),
    '*':(3,0),0:(3,1),"#":(3,2)
}
def distance(l,r,n):
    left_x,left_y = keypad[l][0],keypad[l][1]
    right_x,right_y = keypad[r][0],keypad[r][1]
    n_x,n_y = keypad[n][0],keypad[n][1]

    left_dist=abs(left_x-n_x)+abs(left_y-n_y)
    right_dist=abs(right_x-n_x)+abs(right_y-n_y)

    return left_dist,right_dist

def solution(numbers, hand):
    answer = ''
    left='*'
    right='#'

    for n in numbers:
        #print(left,right,n)
        if n in [1,4,7]:
            answer=answer+"L"
            left=n
        elif n in [3,6,9]:
            answer=answer+"R"
            right=n
        else: #거리가 더 작은쪽을 선택
            #left-n vs right-n 거리비교
            ld,rd=distance(left,right,n)
            if ld<rd: #왼쪽거리가 더 짧으면 왼손을 선택
                answer=answer+"L"
                left=n
            elif ld>rd: #오른쪽거리가 더 짧으면 오른손을 선택
                answer=answer+"R"
                right=n
            elif ld==rd: #비교한 거리가 같으면 hand를 따라감
                if hand=='right':
                    answer=answer+"R"
                    right=n #left는 이전꺼, right는 n
                elif hand=='left':
                    answer=answer+"L"
                    left=n #left는 n, right는 이전꺼
    return answer

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right" #오른손잡이
print(solution(numbers,hand))

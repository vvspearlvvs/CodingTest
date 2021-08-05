def solution(board):
    for i in board:
        for j in range(len(i)):
            print(i[j], "=")
        print("\n")


board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))


def solution(board, moves):
    #FAIL
    
    answer = 0
    basket_stack = []
    board_floor = {1:0,2:0,3:0,4:0,5:0}
    
    #현재 층 계산하기
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] != 0:
                board_floor[col+1] = row
                break        
    print("board_floor :", board_floor)

    #첫번째 move stack으로 옮기기
    board[board_floor[moves[0]]][moves[0]-1] = 0
    board_floor[moves[0]] += 1 
    basket_stack.append(moves[0])
    del moves[0]
    print("move", moves)

    #인형뽑기
    for move in moves:
        if basket_stack[-1:] == board[board_floor[move]][move-1]:
            #스택 top과 뽑은 인형과 동일하면 answer + 1
            answer += 1
        else:
            #다르면 stack에 추가
            basket_stack.append(board[board_floor[move]][move-1])

        board[board_floor[move]][move-1] = 0
        board_floor[move] += 1 
        #print("board : ",board)

    return answer

def solution1(board,moves):
    basket = []
    answer = 0
    for move in moves:
        for index in range(len(board[0])):
            if board[index][move-1] > 0:
                basket.append(board[index][move-1])
                board[index][move-1] = 0
                if basket[-1:] == basket[-2:-1]:
                    #인형이 두개씩 사라잔다.
                    answer += 2
                    basket = basket[:-2]
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
result = solution1(board,moves)
print(result)

"""
print(moves[-1:])
print(moves[-2:-1]) # : 을 이용하면 배열이 나오기때문에 해당 index 값이 없더라도 index out 오류가 발생하지 않는다."""
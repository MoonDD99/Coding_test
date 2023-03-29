def is_win(player, board):
    for row in range(3):
        if all(status == player for status in board[row]):
            return True
    for col in range(3):
        if all(player == board[row][col] for row in range(3)):
            return True
    
    if all(player == board[index][index] for index in range(3)):
        return True
    if all(player == board[index][2-index] for index in range(3)):
        return True
    
    return False
    
def solution(board):
    num_o = sum(row.count('O') for row in board)
    num_x = sum(row.count('X') for row in board)
    
    if num_x > num_o or abs(num_x - num_o) > 1:
        return 0
    if (is_win('O',board) and num_x != num_o-1) or (is_win('X',board) and num_o != num_x):
        return 0
    return 1
    
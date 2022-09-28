def solution(rows, columns, queries):
    answer = []
    board = [[0] * columns for _ in range(rows)]

    num = 1
    for row in range(0,rows):
        for column in range(0,columns):
            board[row][column] = num
            num += 1

    for startRow, startCol, endRow, endCol in queries:
        previous = board[startRow-1][startCol-1]
        minValue = previous

        #위
        for col in range(startCol, endCol):
            next = board[startRow-1][col]
            board[startRow-1][col] = previous
            previous = next
            minValue = min(previous,minValue)
        
        #오른쪽
        for row in range(startRow, endRow):
            next = board[row][endCol-1]
            board[row][endCol-1] = previous
            previous = next
            minValue = min(previous, minValue)
        
        #아래
        for col in range(endCol-2, startCol-2, -1):
            next = board[endRow-1][col]
            board[endRow-1][col] = previous
            previous = next
            minValue = min(previous, minValue)
        
        #오른쪽
        for row in range(endRow-2, startRow-2, -1):
            next = board[row][startCol-1]
            board[row][startCol-1] = previous
            previous = next
            minValue = min(previous, minValue)
                
        answer.append(minValue)    
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

"""rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]"""
result = solution(rows, columns, queries)
print(result)